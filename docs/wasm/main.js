#!/usr/bin/env node
"use strict";

class WasmPython {
  constructor(context) {
    console.log(context);
  }
}

class MainJS {
  #context_file = "./wasm/context.json";

  constructor() {
    (async () => {
      const response = await fetch(this.#context_file);
      if (!response.ok) throw new Error(`fetch error ${this.#context_file}`);
      const context = await response.json();

      new WasmPython(context);
    })();
  }
}

new MainJS();
