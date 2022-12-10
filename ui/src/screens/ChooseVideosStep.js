import { useEffect, useState } from 'react';
import { Box, Container, Typography, TextField, Button } from '@mui/material';
import VideoChooser from '../components/VideoChooser';

const ChooseVideosStep = (props) => {
    const [error, setError] = useState(undefined);
    const [videos, setVideos] = useState([]);
    const [selectedVideos, setSelectedVideos] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:5000//fetch_channel_videos//${props.data.channel_id}`)
            .then((r) => r.json())
            .then((response) => {
                const videoRows = response.items.filter((row) => row.id.kind == 'youtube#video');
                const rows = videoRows.map((row) => {
                    return {
                        id: row.id.videoId,
                        thumbnail: row.snippet.thumbnails.medium.url,
                        title: row.snippet.title,
                        date: row.snippet.publishTime
                    }
                })

                setVideos(rows);
            })
            .catch(function(error) {
                console.log('Request failed', error);
                setError(error);
            });
    }, []);

    const submitSelected = () => {
        console.log('selectedvideos')
        console.log(selectedVideos);
        props.onVideosSelected(selectedVideos);
    }

    return <Container>
        <VideoChooser videos={videos} setSelectedVideos={setSelectedVideos} />
        <Box mt={3}>
            <Button onClick={submitSelected} variant="outlined">Review</Button>
        </Box>
    </Container>
}

export default ChooseVideosStep;

