/* Handle messages from the main thread. */
onmessage = async (event) => {
  console.log("Worker got message:");
  console.log(event.data);
};

console.log("Worker started");

postMessage("What's good from worker!");

// testing

var Module = {
  onRuntimeInitialized: () => {console.log("YUP");}
};

// importScripts("../../build/wasm/apps/test_file.js");
