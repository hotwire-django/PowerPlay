import { Application, Controller} from "./stimulus-strada.js"

Stimulus.register("charlimit", class extends Controller {
  static targets = [ "commentField", "remainingChars" ]
  static values = {
    maxlength: { type: Number, default: 20 },
  }

  connect(){
    this.check()
  }

  check() {
      if(this.commentFieldTarget.value.length >= this.maxLengthValue){
        this.commentFieldTarget.value = this.commentFieldTarget.value.substring(0, this.maxlengthValue)
      }
      this.remainingCharsTarget.innerHTML = (
        `${this.commentFieldTarget.value.length}/${this.maxlengthValue} chars`
      )
  }
})


