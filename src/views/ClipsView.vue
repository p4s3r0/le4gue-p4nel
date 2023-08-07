<template>
        <h1>Videos von die jüngsten Talente</h1>
        <video :src=this.curr_video_link controls>
        <source >
            Your browser does not support the video tag.
        </video> 


<div id="videoSelector">
    <video-strip v-for="vid in this.videos" 
                            :name=vid.name 
                            @click="changeUrlOfVideo(vid.link)"/>
</div>

</template>

<script>
import VideoStrip from '@/components/VideoStrip.vue';
import { getVideos } from '@/db'
export default {
    data() {
        return {
            videos: [],
            curr_video_link: "",
        };
    },
    name: 'ClipsView',
    components: {
        VideoStrip,
    },
    methods: {
        changeUrlOfVideo(link) {
            this.curr_video_link = link;
        }
    }, 
    beforeMount() {
        getVideos().then((res) => {
            this.videos = Object.freeze(res);
            this.curr_video_link = this.videos[0].link
        })
    }
}
</script>

<style scoped>
video {
    width: 70vw;
}

h1 {
    margin-top: 50px;
    color: white;
}


#videoSelector {
    display: flex;
    grid-gap: 10px;
    width: 80%;
    transform: translateX(-50%);
    margin-left: 50vw;
    flex-wrap: wrap;
    justify-content: space-evenly;
}



@media only screen and (max-width: 500px) {

}
</style>
