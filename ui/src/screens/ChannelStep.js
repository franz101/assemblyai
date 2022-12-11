import { useState } from "react";
import {
  Box,
  Button,
  Container,
  Grid,
  Input,
  InputAdornment,
  Typography,
  TextField,
} from "@mui/material";

const UsernameStep = ({ onComplete }) => {
  const [error, setError] = useState(false);

  const verifyHandle = (handle) => {
    if (handle.length < 2) {
      // must use handle that starts with @
      setError(true);
      return;
    }

    const cleanedHandle = handle.replace("@", "");

    fetch(
      `${process.env.REACT_APP_SERVER_HOST}/api/verify_handle/${cleanedHandle}`
    )
      .then((r) => r.json())
      .then((response) => {
        console.log(response);
        onComplete(response);
      })
      .catch(function (error) {
        console.log("Request failed", error);
        setError(true);
      });
  };

  return (
    <Grid container spacing={3} sx={{ pt: 0 }}>
      <Grid item xs={12} sm={6}>
        <TextField
          id="channel"
          name="channel"
          label="YouTube Channel Handle"
          fullWidth
          InputProps={{
            startAdornment: <InputAdornment position="start">@</InputAdornment>,
          }}
          variant="standard"
          autoFocus
          onKeyPress={(e) => {
            const value = e.target.value;
            if (e.key === "Enter") {
              console.log("value");
              console.log(value);
              verifyHandle(value);
            }
          }}
        />
      </Grid>

      {/* <Grid item xs={12} sm={6}>
        <Button onClick={verifyHandle} variant="contained" disableElevation>
          Next
        </Button>
      </Grid> */}
    </Grid>
  );
};

export default UsernameStep;

/* <Container>
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
            
        </Box>
    </Container> */
