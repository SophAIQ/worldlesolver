# WorldleSolver
[Worldle](https://worldle.teuteuf.fr/) is a game where the player guesses the name of the country based on its outline. This is a wonderful game suitable for anyone interested in geography. This program is intended to solve Worldle puzzles automaticaly with no player input. The PyTorch model is trained/tested and stored in the model folder with over 99% testing accuracy. The lack of good data meant the model is overfitted and will give an occassional wrong answer. In this case, I want to also take into account the direction and distance of the guess from the answer. I am thinking about building a graph with each country being a node and the edge as being the distance from each node. I am still figuring out how the direction can be taken into account. 

Country shape dataset is from Github user djaiss repository [mapsicon](https://github.com/djaiss/mapsicon). 

Other useful resources:
[Pytorch Computer Vision](https://www.learnpytorch.io/03_pytorch_computer_vision/)

