import React from 'react';
import Button from '@mui/material/Button';


function ButtonColour (props) {

    return (
        <div style={{display: 'flex'}}>
            <Button id="colour-button" variant="contained" size="large" style={{margin: '20px'}} onClick={props.retrieveColour}>
                Change colours!
            </Button>
        </div>
    )
}


export default ButtonColour;