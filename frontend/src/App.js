import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'axios';
import PokemonDisplay from './components/pokemonDisplay';

// Components
import PokemonSearch from './components/pokemonSearchBar';
import axios from 'axios';

// const pokemonAPI = 'https://pokeapi.co/api/v2/pokemon/';

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
