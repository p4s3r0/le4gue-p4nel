import { createClient } from '@supabase/supabase-js'

export const supabase = createClient('https://lmfbdtnxmqappdpipvhq.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxtZmJkdG54bXFhcHBkcGlwdmhxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY3NzYxMTA0MCwiZXhwIjoxOTkzMTg3MDQwfQ.6WoYz0FgKJGYKolPx2Ej6HTfD1VEb8SN0u8kN0mA2yE')


export async function getSummonerBasicDB(name) {
    name = name.toLowerCase()
    let { data } = await supabase.from('SummonerBasic').select().eq("name", name)

    data = data[0]

    const response = {
        level: data.level
    }
    return response;
}



export async function getSummonerDevDB(name) {
    name = name.toLowerCase()
    let { data } = await supabase.from('SummonerDev').select().eq("name", name)
    data = data[0]

    const response = {
        name: data.name, 
        id: data.id, 
        accountId: data.accountId,
        puuid: data.puuid,
    }
    return response;
}


export async function getSummonerRankInfoSoloDB(name) {
    name = name.toLowerCase()
    let { data } = await supabase.from('SummonerRankedSolo').select().eq("name", name)
    data = data[0]
    if (data == undefined) return false;

    const response = {
        tier: data.tier,
        rank: data.rank,
        wins: data.wins,
        losses: data.losses,
        hotStreak: data.hotStreak,
        LP: data.LP,
        rankedPoints: data.rankedRank,
    }
    return response;
}



export async function getSummonerRankInfoFlexDB(name) {
    name = name.toLowerCase()
    let { data } = await supabase.from('SummonerRankedFlex').select().eq("name", name)
    data = data[0]
    if (data == undefined) return false;

    const response = {
        tier: data.tier,
        rank: data.rank,
        wins: data.wins,
        losses: data.losses,
        hotStreak: data.hotStreak,
        LP: data.LP
    }
    return response;
}
