import * as React from 'react';
import Box from '@mui/material/Box';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import UsernameStep from './ChannelStep';
import ChooseVideosStep from './ChooseVideosStep';

const steps = ['Your Channel', 'Select Videos', 'Review', 'Submitted'];

export default function Steps() {
  const [activeStep, setActiveStep] = React.useState(0);
  const [data, setData] = React.useState(null);

  const handleNext = (data) => {
    setData(data);
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const onVideosSelected = (selected) => {
    setData(selected);
    setActiveStep(2);
  }

  const finalize = () => {
    fetch(`http://127.0.0.1:5000/enqueue_videos`, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        video_ids: data
      }),
    })
    .then((r) => r.json())
    .then((response) => {
        console.log(response);
        setActiveStep(3);
    })
    .catch(function(error) {
        console.log('Request failed', error);
        //setError(true);
    });
  }

  return (
    <Box sx={{ width: '100%' }}>
      <Stepper activeStep={activeStep}>
        {steps.map((label, index) => {
          const stepProps = {};
          const labelProps = {};
          return (
            <Step key={label} {...stepProps}>
              <StepLabel {...labelProps}>{label}</StepLabel>
            </Step>
          );
        })}
      </Stepper>
      <>
        <Typography variant='h4' sx={{ mt: 4, mb: 1 }}>{steps[activeStep]}</Typography>
        <Box sx={{ display: 'flex', flexDirection: 'row', pt: 2 }}>
          <Box sx={{ flex: '1 1 auto' }} />

          {activeStep === 0 &&
            <UsernameStep onComplete={handleNext} />
          }

          {activeStep === 1 && 
            <ChooseVideosStep onVideosSelected={onVideosSelected} data={data} />
          }

          {activeStep === 2 && <div>
              <Box mt={3}>
                We are submitting the following video ID's:
                {data.map((videoId) => {
                  return <div key={videoId}>{videoId}</div>
                })}
                  <Button onClick={finalize} variant="outlined">Submit</Button>
              </Box>
          </div>} 
        </Box>
      </>
    </Box>
  );
}
