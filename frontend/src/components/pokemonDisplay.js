import React from 'react';
import { makeStyles } from '@mui/styles';

// For layouts
import Paper from '@mui/material/Paper';
import Grid from '@mui/material//Grid';


const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        margin: '25px',
    },
    headingPaper: {
        padding: theme.spacing(2),
        margin: theme.spacing(2),
        textAlign: 'center',
        color: 'white',
        fontSize: '20px',
        backgroundColor: '#41729F',
    },
    paper: {
        padding: theme.spacing(2),
        margin: theme.spacing(2),
        textAlign: 'center',
        color: theme.palette.text.primary,
        fontSize: '20px',
        backgroundColor: 'lightblue',
    },
    pokemonHeader: {
        fontFamily: 'pokemon',
        fontSize: '50px', 
        letterSpacing: '0.3rem',
        color: '#ffd700',
        textShadow: '-4px -4px 0 #00578a, 4px -4px 0 #00578a, -4px 4px 0 #00578a, 4px 4px 0 #00578a'
    }
  }));


function PokemonDisplay (props) {

    const classes = useStyles();
    let pokemon = props.pokemonData;

    const capitalise = (string) => {
        return string[0].toUpperCase() + string.substring(1)
    }

    const display = () => {
        if (pokemon.name) {
            return (
                <div className={classes.root}>
                    <Grid container spacing={3}>
                        {/* // Name of Pokemon */}
                        <Grid item xs={12}>
                            <h2 className={classes.pokemonHeader}>{capitalise(pokemon.name)}</h2>
                        </Grid>
                        <Grid container justifyContent="space-evenly">
                            {/* // Image */}
                            <Grid item xs={3} container justifyContent="space-evenly">
                                <img src={pokemon.photo_url} height="225px" alt={`Image of ${pokemon.name}`} />
                            </Grid>
                            {/* // Stats */}
                            <Grid item xs={8} container justifyContent="space-evenly" alignItems="baseline">
                                
                                {/* // Types */}
                                <Grid item xs={4}>
                                    <Paper className={classes.headingPaper}>Type: </Paper>
                                </Grid>
                                <Grid item xs={8} container justifyContent="space-evenly" alignItems="baseline">
                                       <Grid item xs ><Paper className={classes.paper}>{capitalise(pokemon.type1)}</Paper></Grid>
                                    <Grid item xs >
                                        {pokemon.type2 ?
                                        <Paper className={classes.paper}>{capitalise(pokemon.type2)}</Paper> : null}
                                    </Grid>
                                </Grid>

                                {/* // Moves */}
                                <Grid item xs={4}>
                                    <Paper className={classes.headingPaper}>Moves: </Paper>
                                </Grid>
                                <Grid item style={{maxHeight: '410px', overflow: 'auto'}} xs={8} container justifyContent="space-evenly" alignItems="baseline">
                                    {pokemon.moves.map((move, idx) => {
                                        return <Grid item xs={4}><Paper key={idx} className={classes.paper}>{capitalise(move.name)}</Paper></Grid>
                                    })}
                                </Grid>

                            </Grid>
                        </Grid>
                    </Grid>
                </div>
            )
        }
    }

    return (
        <div style={{marginTop: '50px'}}>
            {display()}
        </div>
    )

}

export default PokemonDisplay;