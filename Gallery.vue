<template>
  <div class="app">
    <div v-if="showJson">
      <button @click='showJson = false'>Hide Json</button>
      <p>{{images}}</p>
    </div>
    <div class="enlarge" v-if="enlarge">
        <img @click='enlargeImage(2)' id="enlarged" :src="enlargedImage" alt="">
      </div>
    <div class="jam" v-if="!enlarge">
      <div class='main-container'>
        <div class="buttons">
          <button @click='remove'>Remove</button>
          <button @click='showJson = true'>show JSON</button>
          <p>Total Images: {{images.length}}</p>
        </div>
          <img id='main' @click='enlargeImage(1)' :src="mainImage">
        </div>
      <div class="gallery-container">
        <div>
          <div class='gallery' v-for='image in images.slice(1)' :key='image'>
            <div class="columns">
              <img class="galleryimage" :id="image.id" @click='swap(image.id)' :src='image.url'/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import json from '../json_file/output.json'

export default {
  name: "App",

  data() {
    return{
      images: json,
      jam: [],
      isActive: false,
      enlargedImage: "",
      enlarge: false,
      mainImage: "",
      showJson: false
    }
  },
  created(){
    this.mainImage = this.images[0].url
  },
  methods: {
    swap(e){
      var main = document.getElementById('main')
      var swap = document.getElementById(e)
      main.src = [swap.src, swap.src = main.src][0]
      this.mainImage = main.src

    },
    remove(){
      var main = document.getElementById('main')
      for(let i=0; i<this.images.length;i++){
        if(this.images[i].url == main.src){
          this.images.splice(i, 1)
          main.src = this.images[i].url
          }
        }
      },
      enlargeImage(e){
        if(e == 1){
          this.enlarge = true
          var main = document.getElementById('main')
          this.enlargedImage = main.src
        }
        else{
          this.enlarge = false
        }
      }
  }
}
</script>

<style>

.enlarge{
  margin: auto;
}
#enlarged{
  min-height: 100vh;
  margin: auto;
  display: flex;
}

#main{
  height: auto;
  width: 100%;
  display: block;
  margin: auto;
  align-self: flex-start;
}

.main-container{
  height: 94vh;
  width: 35vw;
  top: 6rem;
  position: sticky;
  position: -webkit-sticky;
}

.gallery{
  display: inline-block;
}
.gallery-container{
  margin: auto;
  width: 50vw;
}

.columns{
  height: 240px;
  min-width: 180px;
  margin: auto;
  display: block;
}

.galleryimage{
  height: 200px;
  width: auto;
  margin: 5%;
  padding: 7%;
  display: block;
  margin: auto;

}

.jam{
  display: flex;
  width: 100vw;
}

body{
  background-color: whitesmoke;
}



</style>

