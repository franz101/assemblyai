import { useState } from 'react';
import { Box, Button, Container, Grid, Input, InputAdornment, Typography, TextField } from '@mui/material';

const UsernameStep = (props) => {
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
                props.onComplete(response);
            })
            .catch(function(error) {
                console.log('Request failed', error);
                setError(true);
            });
    }

    return <Container>
        <Box>
            <Grid container alignItems="center">
                <Grid xs={4}></Grid> 
                <Grid>
                    <Typography variant='h5'>https://youtube.com/&nbsp;</Typography>
                </Grid>

                <Grid xs={2}>
                    <TextField id="handle" label="@youtubehandle" variant="outlined" error={error} />
                </Grid>
                <Grid item alignItems="stretch">
                    &nbsp;&nbsp;
                </Grid>
            </Grid>
        </Box>
        <Box mt={3}>
            <Button onClick={verifyHandle} variant="contained" disableElevation>Next</Button>
        </Box>
    </Container>
}

export default UsernameStep;
