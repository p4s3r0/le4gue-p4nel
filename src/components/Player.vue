<template>

<div id="container">
    <div class="border">

    <div id="position"> <p>#{{ this.position }}</p></div>
            <h1> {{ this.name }}</h1>
            <p> level: {{ this.player_data.level }}</p>
            <div v-if="this.player_data.ranked.solo.LP != '☃'">
                <div id="solo">
                    <p>Solo:</p>
                </div>
                <div id="badge" :class=this.classes.badge_solo >
                    <p>{{ this.player_data.ranked.solo.tier }} {{ this.player_data.ranked.solo.rank }}</p>
                </div>
                <div id="lp" :class=this.classes.border_solo >
                    <p> LP: {{ this.player_data.ranked.solo.LP }}</p>
                </div>
            </div>
            <div v-if="this.player_data.ranked.flex.LP != '☃'" id="flexPos">
                <div id="flex">
                    <p>Flex:</p>
                </div>
                <div id="badge" :class=this.classes.badge_flex >
                    <p>{{ this.player_data.ranked.flex.tier }} {{ this.player_data.ranked.flex.rank }}</p>
                </div>
                <div id="lp" :class=this.classes.border_flex >
                    <p> LP: {{ this.player_data.ranked.flex.LP }}</p>
                </div>
            </div>
            <p id="wrPos" v-if="this.player_data.ranked.solo.LP != -1"> WR: {{ (100 / (this.player_data.ranked.solo.wins + this.player_data.ranked.solo.losses) * this.player_data.ranked.solo.wins).toFixed(1) }}% [ <em id="green">{{ this.player_data.ranked.solo.wins }}</em> / <em id="red">{{ this.player_data.ranked.solo.losses }}</em> ]</p>
    </div>
</div>

</template>
  
<script>
import { getSummonerRank } from '@/db'

export default {
    name: 'Player',
    props: ["name", "ranking", "position"],
    components: {
    },
    data() {
        return {
            classes: {
                badge_solo: "badgeUNRANKED",
                border_solo: "borderUNRANKED",
                badge_flex: "badgeUNRANKED",
                border_flex: "borderUNRANKED"
            },
            player_data: {
                ranked: {
                    flex: {},
                    solo: {}
                },
                level: -1
            },
            
        };
    },
    methods: {
    }, beforeMount() {    
        getSummonerRank(this.name).then( (res) => {
          if (res[0] == null) {
            this.player_data.ranked.solo.LP = "-";
            this.player_data.ranked.solo.tier = "";
            this.player_data.ranked.solo.rank = "UNRANKED";
            this.classes.badge_solo = "badgeUNRANKED"
            this.classes.border_solo = "borderUNRANKED"
          } else {
            this.player_data.ranked.solo = res[0];
            this.classes.badge_solo = "badge" + res[0].tier
            this.classes.border_solo = "border" + res[0].tier
          }


          if (res[1] == null) {
            this.player_data.ranked.flex.LP = "-";
            this.player_data.ranked.flex.tier = "";
            this.player_data.ranked.flex.rank = "UNRANKED";
            this.classes.badge_flex = "badgeUNRANKED"
            this.classes.border_flex = "borderUNRANKED"
          } else {
            this.player_data.ranked.flex = res[1];
            this.classes.badge_flex = "badge" + res[1].tier
            this.classes.border_flex = "border" + res[1].tier
          }
          this.player_data.level = res[2].level
        });
        
    }
}
</script>
<style scoped>
#container {
    position: relative;
    border: solid 1px #2b2a2a;
    box-shadow: rgba(0, 0, 0, 1) 0px 10px 30px;
    /* From https://css.glass */
    background: rgba(10, 10, 10, 0.5);
    border-radius: 10px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(11.2px);
    -webkit-backdrop-filter: blur(11.2px);
    border: 1px solid rgba(0, 0, 0, 0.24);
    width: 300px;
}


#flexPos {
  margin-top: -10px;
}

#wrPos {
  margin-top: -10px;
}

#lp{
    text-align: center;
    display: inline-block;
    font-weight: bolder;
    height: 20px;
    padding-left: 5px;
    padding-right: 5px;
    margin-left: 10px;
}
#lp p {
    background-color: transparent;
    transform: translateY(-63%);
    font-size: 0.9em;
}

#solo {
    display: inline-block;
    background-color: transparent;
}
#solo p{
    text-align: center;
    transform: translateY(-50%);
    margin-right: 5px;
}

#flex {
    display: inline-block;
    background-color: transparent;
}
#flex p{
    text-align: center;
    transform: translateY(-50%);
    margin-right: 5px;
}

div {
    background-color: transparent;
}

#position {
    position: absolute;
    width: 40px;
    height: 40px;
    top: -20px;
    right: -20px;
    border-radius: 40px;
    background: rgba(255, 255, 255, 0.5);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(11.2px);
    -webkit-backdrop-filter: blur(11.2px);
    color: black;
    font-size: 1.5em;
}

#position p {
    transform: translateY(-60%);
}

#badge {
    display: inline-block;
    text-align: center;
    height: 25px;
    border-radius: 5px;
    padding-right: 10px;
    padding-left: 10px;
}
#badge p {
    color: black;
    background-color: transparent;
    transform: translateY(-55%);
}
.border {
    padding: 1px;
    border-radius: 10px;
    background: rgb(22, 22, 38);
}
.border::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 50%;
  height: 50%;
  -webkit-box-shadow: 0 0 17px 3px #ffff01,0 0 4px 2px #ffff01;
          box-shadow: 0 0 17px 3px #ffff01,0 0 4px 2px #ffff01;
  z-index: -9999;
  -webkit-animation-name: yellow-shadow;
          animation-name: yellow-shadow;
  -webkit-animation-timing-function: ease;
          animation-timing-function: ease;
  -webkit-animation-duration: 4s;
          animation-duration: 4s;
  -webkit-animation-iteration-count: infinite;
          animation-iteration-count: infinite;
  border-radius: 5px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
}

.border::after {
  content: '';
  position: absolute;
  right: 0;
  bottom: 0;
  width: 50%;
  height: 50%;
  -webkit-box-shadow: 0 0 17px 3px #0ff,0 0 4px 2px #0ff;
          box-shadow: 0 0 17px 3px #0ff,0 0 4px 2px #0ff;
  z-index: -999;
  -webkit-animation-name: cyan-shadow;
          animation-name: cyan-shadow;
  -webkit-animation-timing-function: ease;
          animation-timing-function: ease;
  -webkit-animation-duration: 4s;
          animation-duration: 4s;
  -webkit-animation-iteration-count: infinite;
          animation-iteration-count: infinite;
  border-radius: 5px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
}


@-webkit-keyframes yellow-shadow {
  0% {
    top: 0;
    left: 0;
  }
  25% {
    top: 50%;
    left: 0;
  }
  50% {
    top: 50%;
    left: 50%;
  }
  75% {
    top: 0;
    left: 50%;
  }
  100% {
    top: 0;
    left: 0;
  }
}

@keyframes yellow-shadow {
  0% {
    top: 0;
    left: 0;
  }
  25% {
    top: 50%;
    left: 0;
  }
  50% {
    top: 50%;
    left: 50%;
  }
  75% {
    top: 0;
    left: 50%;
  }
  100% {
    top: 0;
    left: 0;
  }
}

@-webkit-keyframes cyan-shadow {
  0% {
    right: 0;
    bottom: 0;
  }
  25% {
    right: 0;
    bottom: 50%;
  }
  50% {
    right: 50%;
    bottom: 50%;
  }
  75% {
    right: 50%;
    bottom: 0;
  }
  100% {
    right: 0;
    bottom: 0;
  }
}

@keyframes cyan-shadow {
  0% {
    right: 0;
    bottom: 0;
  }
  25% {
    right: 0;
    bottom: 50%;
  }
  50% {
    right: 50%;
    bottom: 50%;
  }
  75% {
    right: 50%;
    bottom: 0;
  }
  100% {
    right: 0;
    bottom: 0;
  }
}

@-webkit-keyframes gradient-shadow {
  0% {
    -webkit-box-shadow: 0 0 17px 3px #C586C0,0 0 4px 2px #C586C0;
            box-shadow: 0 0 17px 3px #C586C0,0 0 4px 2px #C586C0;
  }
  20% {
    -webkit-box-shadow: 0 0 17px 3px #0ff,0 0 4px 2px #0ff;
            box-shadow: 0 0 17px 3px #0ff,0 0 4px 2px #0ff;
  }
  40% {
    -webkit-box-shadow: 0 0 17px 3px #0f0,0 0 4px 2px #0f0;
            box-shadow: 0 0 17px 3px #0f0,0 0 4px 2px #0f0;
  }
  60% {
    -webkit-box-shadow: 0 0 17px 3px #ffff01,0 0 4px 2px #ffff01;
            box-shadow: 0 0 17px 3px #ffff01,0 0 4px 2px #ffff01;
  }
  80% {
    -webkit-box-shadow: 0 0 17px 3px #f00,0 0 4px 2px #f00;
            box-shadow: 0 0 17px 3px #f00,0 0 4px 2px #f00;
  }
  100% {
    -webkit-box-shadow: 0 0 17px 3px #C586C0,0 0 4px 2px #C586C0;
            box-shadow: 0 0 17px 3px #C586C0,0 0 4px 2px #C586C0;
  }
}

@keyframes gradient-shadow {
  0% {
    -webkit-box-shadow: 0 0 17px 3px #C586C0,0 0 4px 2px #C586C0;
            box-shadow: 0 0 17px 3px #C586C0,0 0 4px 2px #C586C0;
  }
  20% {
    -webkit-box-shadow: 0 0 17px 3px #0ff,0 0 4px 2px #0ff;
            box-shadow: 0 0 17px 3px #0ff,0 0 4px 2px #0ff;
  }
  40% {
    -webkit-box-shadow: 0 0 17px 3px #0f0,0 0 4px 2px #0f0;
            box-shadow: 0 0 17px 3px #0f0,0 0 4px 2px #0f0;
  }
  60% {
    -webkit-box-shadow: 0 0 17px 3px #ffff01,0 0 4px 2px #ffff01;
            box-shadow: 0 0 17px 3px #ffff01,0 0 4px 2px #ffff01;
  }
  80% {
    -webkit-box-shadow: 0 0 17px 3px #f00,0 0 4px 2px #f00;
            box-shadow: 0 0 17px 3px #f00,0 0 4px 2px #f00;
  }
  100% {
    -webkit-box-shadow: 0 0 17px 3px #C586C0,0 0 4px 2px #C586C0;
            box-shadow: 0 0 17px 3px #C586C0,0 0 4px 2px #C586C0;
  }
}

@-webkit-keyframes half-yellow-shadow {
  0% {
    top: 0;
    left: 0;
    height: 50%;
    width: 50%;
  }
  16.66% {
    top: 0;
    left: 0;
    height: 50%;
    width: 100%;
  }
  32.32% {
    top: 0;
    left: 50%;
    height: 50%;
    width: 50%;
  }
  49.98% {
    top: 50%;
    left: 50%;
    height: 50%;
    width: 50%;
  }
  66.64% {
    top: 50%;
    left: 0;
    height: 50%;
    width: 100%;
  }
  83.3% {
    top: 50%;
    left: 0;
    height: 50%;
    width: 50%;
  }
  100% {
    top: 0;
    left: 0;
    height: 50%;
    width: 50%;
  }
}

@keyframes half-yellow-shadow {
  0% {
    top: 0;
    left: 0;
    height: 50%;
    width: 50%;
  }
  16.66% {
    top: 0;
    left: 0;
    height: 50%;
    width: 100%;
  }
  32.32% {
    top: 0;
    left: 50%;
    height: 50%;
    width: 50%;
  }
  49.98% {
    top: 50%;
    left: 50%;
    height: 50%;
    width: 50%;
  }
  66.64% {
    top: 50%;
    left: 0;
    height: 50%;
    width: 100%;
  }
  83.3% {
    top: 50%;
    left: 0;
    height: 50%;
    width: 50%;
  }
  100% {
    top: 0;
    left: 0;
    height: 50%;
    width: 50%;
  }
}

@-webkit-keyframes half-cyan-shadow {
  0% {
    bottom: 0;
    right: 0;
    height: 50%;
    width: 50%;
  }
  16.66% {
    bottom: 0;
    right: 0;
    height: 50%;
    width: 100%;
  }
  32.32% {
    bottom: 0;
    right: 50%;
    height: 50%;
    width: 50%;
  }
  49.98% {
    bottom: 50%;
    right: 50%;
    height: 50%;
    width: 50%;
  }
  66.64% {
    bottom: 50%;
    right: 0;
    height: 50%;
    width: 100%;
  }
  83.3% {
    bottom: 50%;
    right: 0;
    height: 50%;
    width: 50%;
  }
  100% {
    bottom: 0;
    right: 0;
    height: 50%;
    width: 50%;
  }
}

@keyframes half-cyan-shadow {
  0% {
    bottom: 0;
    right: 0;
    height: 50%;
    width: 50%;
  }
  16.66% {
    bottom: 0;
    right: 0;
    height: 50%;
    width: 100%;
  }
  32.32% {
    bottom: 0;
    right: 50%;
    height: 50%;
    width: 50%;
  }
  49.98% {
    bottom: 50%;
    right: 50%;
    height: 50%;
    width: 50%;
  }
  66.64% {
    bottom: 50%;
    right: 0;
    height: 50%;
    width: 100%;
  }
  83.3% {
    bottom: 50%;
    right: 0;
    height: 50%;
    width: 50%;
  }
  100% {
    bottom: 0;
    right: 0;
    height: 50%;
    width: 50%;
  }
}


#green {
    color: #6eec47;
    font-style: normal;
}
#red {
    color: red;
    font-style: normal;
}

.badgeMASTER {
    background-color: rgb(194, 82, 194);
}
.badgeDIAMOND {
    background-color: rgb(77, 111, 223);
}
.badgePLATINUM {
    background-color: rgb(53, 148, 177);
}
.badgeGOLD {
    background-color: #FFD700;
}
.badgeSILVER {
    background-color: silver;
}
.badgeBRONZE {
    background-color: rgb(219, 130, 47);
}

.badgeUNRANKED {
    background-color: rgb(255, 255, 255);
}


.borderMASTER {
    border: solid rgb(194, 82, 194) 2px;
    border-radius: 5px;
}
.borderDIAMOND {
    border: solid rgb(77, 111, 223) 2px;
    border-radius: 5px;
}
.borderPLATINUM {
    border: solid rgb(53, 148, 177) 2px;
    border-radius: 5px;
}
.borderGOLD {
    border: solid #FFD700 2px;
    border-radius: 5px;
}
.borderSILVER {
    border: solid silver 2px;
    border-radius: 5px;
}
.borderBRONZE {
    border: solid rgb(219, 130, 47) 2px;
    border-radius: 5px;
}

.borderUNRANKED {
    border: solid rgb(255, 255, 255) 2px;
    border-radius: 5px;
}


</style>
  