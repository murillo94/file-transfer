const readline = require('readline');
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = '> ';
const output = '< ';

const PROTO_PATH = __dirname + '/../proto/message.proto';
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
});

const message_proto = grpc.loadPackageDefinition(packageDefinition).rpc;

function main() {
  const client = new message_proto.Fetch(
    'localhost:9778',
    grpc.credentials.createInsecure()
  );

  rl.on('line', function(value) {
    client.Capitalize({ data: [...Buffer(value)] }, function(err, response) {
      console.log(response.data.toString('utf8'));
      rl.setPrompt(input, input.length);
      rl.prompt();
    });
    rl.setPrompt(output, output.length);
    rl.prompt();
  }).on('close', function() {
    process.exit(0);
  });

  rl.setPrompt(input, input.length);
  rl.prompt();
}

main();
