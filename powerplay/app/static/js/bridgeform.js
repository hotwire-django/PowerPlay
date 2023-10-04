import { Application, Controller, BridgeComponent, BridgeElement} from "./stimulus-strada.js"

Stimulus.register("bridgeform", class extends BridgeComponent {
  static component = "form"
  static targets = [ "submit" ]

  connect() {
    super.connect()
    this.notifyBridgeOfConnect()
  }

  notifyBridgeOfConnect() {
    const submitButton = new BridgeElement(this.submitTarget)
    const submitTitle = submitButton.title

    this.send("connect", { submitTitle }, () => {
      this.submitTarget.click()
    })
  }

  submitStart(event) {
    this.submitTarget.disabled = true
    this.send("submitDisabled")
  }

  submitEnd(event) {
    this.submitTarget.disabled = false
    this.send("submitEnabled")
  }

});


Stimulus.register("bridge--menu", class extends BridgeComponent {
  static component = "menu"
  static targets = [ "title", "item" ]

  show(event) {
    if (this.enabled) {
      event.stopImmediatePropagation()
      this.notifyBridgeToDisplayMenu(event)
    }
  }

  notifyBridgeToDisplayMenu(event) {
    const title = new BridgeElement(this.titleTarget).title
    const items = this.makeMenuItems(this.itemTargets)

    this.send("display", { title, items }, message =>  {
      const selectedIndex = message.data.selectedIndex
      const selectedItem = new BridgeElement(this.itemTargets[selectedIndex])

      selectedItem.click()
    })
  }

  makeMenuItems(elements) {
    const items = elements.map((element, index) => this.menuItem(element, index))
    const enabledItems = items.filter(item => item)

    return enabledItems
  }

  menuItem(element, index) {
    const bridgeElement = new BridgeElement(element)

    if (bridgeElement.disabled) return null

    return {
      title: bridgeElement.title,
      index: index
    }
  }
});

Stimulus.register("bridgeoverflowmenu", class extends BridgeComponent {
  static component = "overflow-menu"

  connect() {
    super.connect()
    this.notifyBridgeOfConnect()
  }

  notifyBridgeOfConnect() {
    const label = this.bridgeElement.title

    this.send("connect", { label }, () => {
      this.bridgeElement.click()
    })
  }

});
