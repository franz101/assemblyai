import { useEffect, useState } from 'react';
import { Container, Typography, TextField, Button } from '@mui/material';
import VideoChooser from '../components/VideoChooser';

const ChooseVideosStep = (props) => {
    const [error, setError] = useState(false);
    const [videos, setVideos] = useState([]);

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
                setError(true);
            });
      }, []);

    return <Container>
        <VideoChooser videos={videos} />
    </Container>
}

export default ChooseVideosStep;

