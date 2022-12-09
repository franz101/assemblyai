import logo from './logo.svg';
import './App.css';
import { Container, Typography, TextField} from '@mui/material';
import Steps from './screens/Steps';
import { useEffect } from 'react';

function App() {
  return (
    <div className="App">
      <Typography variant='h1'>tube2blog</Typography>

      <Container>
        <Steps />
      </Container>

    </div>
  );
}

export default App;
