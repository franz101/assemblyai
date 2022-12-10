import logo from './logo.svg';
import './App.css';
import { Container, Typography, TextField} from '@mui/material';
import Steps from './screens/Steps';
import { useEffect } from 'react';

function App() {
  return (
    <div className="App">
      <Typography variant='h2' mb={5}>streamline</Typography>

      <Container mt={3}>
        <Steps />
      </Container>

    </div>
  );
}

export default App;
