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

const prompt = value => {
  rl.setPrompt(value, value.length);
  rl.prompt();
};

const main = () => {
  const client = new message_proto.Fetch(
    'localhost:9778',
    grpc.credentials.createInsecure()
  );

  rl.on('line', value => {
    client.Capitalize({ data: [...Buffer(value)] }, (err, response) => {
      console.log(response.data.toString('utf8'));
      prompt(input);
    });
    prompt(output);
  }).on('close', () => {
    process.exit(0);
  });

  prompt(input);
};

main();
