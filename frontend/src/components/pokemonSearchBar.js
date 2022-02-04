import React from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';


function PokemonSearch (props) {

    const [pokemon, setPokemon] = React.useState('');

    const findPokemon = (event) => {
        props.searchPokemon(pokemon.toLowerCase());
    }

    return (
        <div style={{display: 'flex'}}>
            <form noValidate autoComplete="off">
                <TextField 
                    style={{backgroundColor: 'lightgrey', margin: '25px 30px'}}
                    id="pokemon-search-bar" 
                    label="Pokémon" 
                    variant="filled"
                    onChange={(e) => setPokemon(e.target.value)}
                />
            </form>
            <Button style={{margin: '25px 30px'}}
                    id="pokemon-search-button" variant="contained" size="large" onClick={findPokemon}>
                Catch
            </Button>
        </div>
    )
}


export default PokemonSearch;