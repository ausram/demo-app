import React from 'react';
import './App.css';
import axios from 'axios';

// Components
import PokemonSearch from './components/pokemonSearchBar';
import PokemonDisplay from './components/pokemonDisplay';


function App() {

    const [pokemonData, setPokemonData] = React.useState({});

    const searchPokemon = (pokemon) => {
        axios.get(`http://localhost:8000/api/pokemon/` + pokemon + '/')
             .then(result => {
                 setPokemonData(result.data);
            })
            .catch(err => {
                alert(`Pokemon "${[pokemon]}" doesn't exist, buddy.`);
                setPokemonData({});
                console.log(err);
            })
        }

    return (
        <div className="App">
            <header className="App-header">
                <PokemonSearch searchPokemon={searchPokemon}/>
                <PokemonDisplay pokemonData={pokemonData}/>
            </header>
        </div>
    );
}

export default App;
