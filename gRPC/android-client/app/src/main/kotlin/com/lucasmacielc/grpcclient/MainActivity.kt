package com.lucasmacielc.grpcclient

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import com.google.protobuf.ByteString
import com.lucasmacielc.grpc.FetchGrpc
import com.lucasmacielc.grpc.Payload
import io.grpc.ManagedChannel
import io.grpc.ManagedChannelBuilder
import io.reactivex.Single
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*
import java.nio.charset.Charset

class MainActivity : AppCompatActivity() {

    private lateinit var channel: ManagedChannel


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        send_button.setOnClickListener {

            channel = ManagedChannelBuilder.forAddress(getHost(), getPort()).usePlaintext().build()

            val stub = FetchGrpc.newBlockingStub(channel)

            val request = Payload.newBuilder()
                .setData(getData())
                .build()

            Single
                .create<Payload> {
                    it.onSuccess(stub.capitalize(request))
                }.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(
                    {
                        textView_grpc_response.text = (
                                it.data.toString(Charset.defaultCharset()) + "\n\n"
                                        + textView_grpc_response.text
                                )
                    },
                    { Log.e("TESTE", "12312321321", it) }
                )
        }
    }

    private fun getHost(): String {
        return editText_host.text.toString()
    }

    private fun getPort(): Int {
        return editText_port.text.toString().toInt()
    }

    private fun getData(): ByteString {
        return ByteString.copyFrom(editText_message.text.toString().toByteArray())
    }
}
