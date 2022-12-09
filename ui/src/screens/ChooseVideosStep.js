import { useState } from 'react';
import { Container, Typography, TextField, Button } from '@mui/material';

const ChooseVideosStep = (props) => {
    const [error, setError] = useState(false);

    console.log('props for choose videos')
    console.log(props);

    return <Container>
        videoChooser
    </Container>
}

export default ChooseVideosStep;
