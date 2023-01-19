import React, { useState } from "react";
import axios from "axios";
import { Box, Skeleton, Heading } from "@chakra-ui/react";
import { SearchBar } from "../components/search-bar";
import { SongCard } from "../components/song-card";

const fetch = async (payload) => {
    try {
        const res = await axios.post("http://localhost:5000/search", payload);
        console.log(res.data.results);
        return {
            results: res.data.results,
            hits: res.data.hits,
        };
    } catch (error) {
        return {
            error: error,
            message: error.response.data.message,
        };
    }
};

const LoadingSkelton = () => {
    return (
        <div>
            <Skeleton h="200px" mx={6} my={4} borderRadius={10} />
            <Skeleton h="200px" mx={6} mb={4} borderRadius={10} />
            <Skeleton h="200px" mx={6} borderRadius={10} />
        </div>
    );
};

const Main = () => {
    const [isSearched, setIsSearched] = useState(false);
    const [songs, setSongs] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [hits, setHits] = useState(0);
    const onSubmit = async (query) => {
        setIsLoading(true);
        const { results, hits } = await fetch(query);
        setIsLoading(false);
        setIsSearched(true);
        setSongs(results);
        setHits(hits);
    };
    return (
        <Box minHeight="100vh" minW="90vw" justify="center">
            <Box px={8} py={4} justify="center" borderRadius={10} width="full" bg="whitesmoke" boxShadow="2xl">
                <Heading justify="center">Sinhala Movie Lyrics and Metaphors</Heading>
                <SearchBar placeholder={"Search for your query........."} onSubmit={onSubmit} />
            </Box>
            {isLoading && <LoadingSkelton />}
            <Box m="6" p="4">
                {isSearched && !isLoading && <Results songs={songs} hits={hits} />}
            </Box>
        </Box>
    );
};

const Results = ({ songs, isLoading, hits }) => {
    return songs.length > 0 ? (
        <div>
            {hits > 10 && <div>{`${hits} results for the search query`}</div>}
            {songs.map((song, index) => (
                <SongCard key={index} songInfo={song._source} />
            ))}
        </div>
    ) : (
        <div>No results for the search query</div>
    );
};

export default Main;
