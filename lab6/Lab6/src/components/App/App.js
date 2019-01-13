import React from 'react';
import { hot } from 'react-hot-loader';
import axios from 'axios';
import Title from './components/Title/Title';
import ListItem from './components/ListItem';

import './styles.css';

export class App extends React.Component {
    constructor(props) {
        super(props);

        this.colorsArray = ['red', 'gold', 'blue']
        this.russifiedColors = ['чёрный', 'синий', 'красный']

        this.colorCounter = 0

        this.state = {
            title: 'Список репозиториев',
            color: this.colorsArray[this.colorCounter],
            repos: [],
            isLoading: false,
        };

        this.onChangeColor = this.onChangeColor.bind(this);
        this.onRepoClick = this.onRepoClick.bind(this);
    }

    componentDidMount() {
        this.setState({
            isLoading: true
        });

        axios.get('https://api.github.com/users/nigraforce/repos')
            .then(response => ({
                repos: response.data,
                isLoading: false
            }))
            .catch(error => ({ isLoading: false }))
            .then(data => this.setState(data));
    }

    onChangeColor() {
    if (++this.colorCounter >= this.colorsArray.length) {
            this.colorCounter = 0
        }
        var tempColor = this.colorsArray[this.colorCounter]
        this.setState({
            color: this.state.color = tempColor
        });
    }

    onRepoClick(repo) {
        this.setState({
            title: repo.name
        })
    }

    render() {
        const {
            color,
            title,
            repos,
            isLoading
        } = this.state;

        return (
            <div>
                <Title color={ color }>
                    { title }
                </Title>

                { isLoading && <h4>Loading...</h4> }

                { repos.map((repo) => (
                        <ListItem
                            key={ repo.id }
                            repo={ repo }
                            onRepoClick={ this.onRepoClick }
                        />
                )) }

                <button onClick={ this.onChangeColor }>Поменять цвет на { this.russifiedColors[this.colorCounter] }</button>
            </div>
        )
    }
}

export default hot(module)(App);
