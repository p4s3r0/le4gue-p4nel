import { AXIOS_BASE_URL } from '@/main.js'
import axios from 'axios';


export async function getBackendStatus() {
    const res = await axios.get(AXIOS_BASE_URL + "get_backend_status")
    return res.data.status;
}

export async function getSummonerRank(name) {
    const res = await axios.get(AXIOS_BASE_URL + "get_summoner_info", { params: {
        name: name
    }})
    return res.data
}


export async function getRanking() {
    const res = await axios.get(AXIOS_BASE_URL + "get_ranking")
    return res.data
}


export async function getVideos() {
    const res = await axios.get(AXIOS_BASE_URL + "get_videos")
    return res.data
}