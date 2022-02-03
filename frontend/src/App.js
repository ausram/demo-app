import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

// Components
import PokemonSearch from './components/pokemonSearchBar';
import PokemonDisplay from './components/pokemonDisplay';
import ButtonColour from './components/buttonColour';


function App() {

    const [pokemonData, setPokemonData] = React.useState({});
    const [buttonColour, setButtonColour] = React.useState(null)
    const [showColourButton, setShowColourButton] = React.useState(false)

    const searchPokemon = (pokemon) => {
        axios.get(`http://localhost:8000/api/pokemon/` + pokemon + '/')
             .then(result => {
                 setPokemonData(result.data);
                 setShowColourButton(true)
            })
            .catch(err => {
                alert(`Pokemon "${[pokemon]}" doesn't exist, buddy.`);
                setPokemonData({});
                console.log(err);
            })
        }
    const retrieveColour = (pokemon) => {
        if (pokemonData) {
            axios.get(`http://localhost:8000/api/pokemon/change-colour/` + pokemonData.id + '/')
                 .then(result => {
                     setButtonColour(result.data);
                })
                .catch(err => {
                    setShowColourButton(false)
                    alert(`Something has gone horribly wrong`);
                    console.log(err);
                })
            } else {}
    }

    return (
        <div className="App">
            <header className="App-header">
                <PokemonSearch searchPokemon={searchPokemon}/>
                {showColourButton ?
                    <ButtonColour retrieveColour={retrieveColour}/> : null}
                <PokemonDisplay pokemonData={pokemonData} buttonColour={buttonColour}/>
            </header>
        </div>
    );
}

export default App;
