<template>
        <h1>League Elite Südtirol + Graz</h1>
        <div id="playersContainer">
            <player v-for="(sum, index) in summoners"
                    :key="sum.ranking"
                    :name="sum.name" 
                    :ranking="sum.ranking" 
                    :position="index+1"/>
    
        </div>
        <p id="clips" @click="this.$router.push('/clips')">MVP Clips von die Jungs</p>

        <div id="backend">
            <p>
                BACKEND_STATUS &nbsp
                <svg height="30" width="30">
                    <circle cx="15" cy="15" r="14" :fill="this.backend_status" />
                </svg> 
            </p>
            
        </div>
</template>

<script>
import Player from "../components/Player.vue";

import { getBackendStatus, getRanking } from "@/db"
export default {
    name: 'MainView',
    components: {
        Player,
    },
    data() {
        return {
            summoners: [],
            backend_status: false
        };
    },
    methods: {
    }, beforeMount() {
        getRanking().then( (res_rank) => {
                this.summoners = Object.freeze(res_rank.sort((a, b) => (a.ranking > b.ranking) ? -1 : 1))
        });

        getBackendStatus().then((res) => {
            if (res == true) {
                this.backend_status = "#16FF00";
            } else {
                this.backend_status = "red";
            }
        })
    }
}
</script>

<style scoped>
* {
    color: white;
}

h1 {
    color: white;
    margin: 50px 80px;
    font-size: 3em;
}
#backend {
    position: absolute;
    right: 0px;
    top: -10px;
    background: rgb(22, 22, 38);
    border-radius: 5px;
    padding-left: 10px;
    padding-right: 10px;
}

svg {
    transform: translateY(25%);
}


#clips {
    margin-left: 30vw;
    font-size: 2em;
    height: 100px;
    width: 40vw;
    text-align: center;
    line-height: 100px;
    user-select: none;

    border-radius: 40px;
    background: rgba(255, 255, 255, 0.5);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(11.2px);
    -webkit-backdrop-filter: blur(11.2px);
    color: black;
    cursor: pointer;
}


#playersContainer {
    display: flex;
    grid-gap: 60px;
    justify-content: space-evenly;
    transform: translateX(-53%);
    margin-left: 50vw;
    margin-top: 5vw;
    width: 80vw;
    margin-bottom: 100px;
    flex-wrap: wrap;
}

</style>
