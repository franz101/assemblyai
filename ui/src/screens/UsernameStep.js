import { useState } from 'react';
import { Container, Typography, TextField, Button } from '@mui/material';

const UsernameStep = () => {
    const [error, setError] = useState(false);

    const verifyHandle = () => {
        const handle = document.getElementById('handle').value;
        if (handle[0] !== '@') {
            // must use handle that starts with @
            setError(true);
            return;
        }

        fetch(`http://127.0.0.1:5000/verify_handle/${handle}`)
            .then((r) => r.json())
            .then((response) => {
                console.log(response);
            })
            .catch(function(error) {
                console.log('Request failed', error);
                setError(true);
            });
    }

    return <Container>
        <Typography>https://youtube.com/</Typography>
        <TextField id="handle" label="@yourchannel" variant="outlined" error={error} />
        <Container>
            <Button onClick={verifyHandle} variant="outlined">Verify</Button>
        </Container>
    </Container>
}

export default UsernameStep;
