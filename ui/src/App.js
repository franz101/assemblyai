import logo from './logo.svg';
import './App.css';
import { Container, Typography, TextField} from '@mui/material';

function App() {
  return (
    <div className="App">
      <Typography variant='h1'>tube2blog</Typography>

      <Container>
        https://youtube.com/
        <TextField id="outlined-basic" label="@yourchannel" variant="outlined" />
      </Container>
    </div>
  );
}

export default App;
