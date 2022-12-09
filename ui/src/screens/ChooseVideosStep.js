import { useState } from 'react';
import { Container, Typography, TextField, Button } from '@mui/material';
import VideoChooser from '../components/VideoChooser';

const ChooseVideosStep = (props) => {
    const [error, setError] = useState(false);

    console.log('props for choose videos')
    console.log(props);

    return <Container>
        <VideoChooser />
    </Container>
}

export default ChooseVideosStep;

