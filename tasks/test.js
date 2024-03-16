console.log("YUPP!!!");

const myWorker = new Worker("build/wasm/apps/worker.js");
// const myWorker = new Worker("tasks/worker.js");

myWorker.postMessage("SUP BUD (from main thread).");

myWorker.onmessage = (e) => {
  console.log("Message received from worker!! Let's go!");
};
