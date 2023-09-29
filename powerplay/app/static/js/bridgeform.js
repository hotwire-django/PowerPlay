import { Application, Controller, BridgeComponent, BridgeElement} from "./stimulus-strada.js"

Stimulus.register("bridgeform", class extends BridgeComponent {
  static component = "form"
  static targets = [ "submit", "counter"]

  submitTargetConnected(target) {
    const submitButton = new BridgeElement(target)
    const submitTitle = submitButton.title
    console.info(submitButton);
    console.info(submitTitle);
    console.info("Connected");
    this.send("connect", { submitTitle }, () => {
      console.info("this.send(connect)");
      target.click()
    })
  }

});
