import { Container, Typography, TextField, Button } from '@mui/material';

const UsernameStep = () => {

    const submitUsername = () => {
        const username = document.getElementById('username').value;
        fetch(`http://127.0.0.1:5000/verify_handle/${username}`)
            .then((r) => r.json())
            .then((response) => {
                console.log(response);
            })
    }

    return <Container>
        <Typography>https://youtube.com/</Typography>
        <TextField id="username" label="@yourchannel" variant="outlined" />
        <Container>
            <Button onClick={submitUsername} variant="outlined">Verify</Button>
        </Container>
    </Container>
}

export default UsernameStep;
