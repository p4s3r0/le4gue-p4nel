<template>
    <div id="containerVideoStrip">
        <img src="../../public/strip.png"/>
        <p> {{ this.name }}</p>
    </div>
</template>
  
<script>
export default {
    name: 'Player',
    props: ["name"],
    components: {
    },
    data() {
        return {
        };
    },

}
</script>
<style scoped>
img {
    width: 400px;
    height: 300px;
    filter: invert();
}

#containerVideoStrip{
    position: relative;
    cursor: pointer;
    width: 400px;
}

p {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -80%);
    font-size: 2em;
    color: white;
}

@media only screen and (max-width: 500px) {
    img {
        width: 300px;
        height: 150px;
    }

    p {
        top: 25px;
        transform: translate(-50%, 0%);
        font-size: 1.5em;
    }
    #containerVideoStrip{
        min-width: auto;
    }
}

</style>
  