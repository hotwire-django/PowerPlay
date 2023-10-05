import { Application, Controller} from "./stimulus-strada.js"

window.Stimulus = Application.start()

Stimulus.register("musicplayer", class extends Controller {
  static targets = [ "audio", "image", "title"]
  connect(){
    //console.info("MusicPlayer Controller connected");
  }

  hide(){
    this.audioTarget.pause();
    this.element.classList.add("d-none")
  }

  setAndPlay(title, image, music_path){
    this.titleTarget.innerHTML = title;
    this.imageTarget.src = image;
    this.audioTarget.src = music_path
    this.audioTarget.play()
    this.element.classList.remove("d-none")
  }
});

Stimulus.register("playbutton", class extends Controller {
  static values = {title: String, image: String, file: String }
  set(){
    const musicController = window.Stimulus.getControllerForElementAndIdentifier(document.getElementById("musicplayer_id"), "musicplayer")
    if(musicController){
      musicController.setAndPlay(this.titleValue, this.imageValue, this.fileValue);
    }else{
      console.error("Could not find element #musicplayer_id")
    }
  }
});
