# WorldleSolver
[Worldle](https://worldle.teuteuf.fr/) is a game where the player guesses the name of the country based on its outline. This is a wonderful game suitable for anyone interested in geography. This program is intended to solve Worldle puzzles automaticaly with no player input. The first guess is made by a computer vision model trained on mapsicon database (see below for link). The PyTorch model is trained/tested and stored in the model folder with over 99% testing "accuracy". Since the dataset is relatively small, the model is overfitted. To me (at this time), this problem is acceptable as Worldle gives the player a total of six guesses and most guesses are correct. If the first answer is incorrect, I want to take into account the direction and distance of the guess from the answer. It would be a good idea to retain the model if the answer is incorrect. Worldle will provide the player this information if the guess is incorrect. To accomplish this, I am thinking about building a graph with each country being a node and the edge as being the distance from each node. I am still figuring out how the direction can be taken into account. 

**To run**\
Run countryshape_solver.py, it will interact with the Worldle website, take a snip of the country from the screen (i didn't want to download the image from the website to avoid unnecessary traffic onto the dev website), clean up the image and store it on the computer. It will then pass the image to the predict.py function and retrieve the guess. It will then type the prediction into the website and submit. At this time, it will then close the webpage. Next steps are to verify the answer and do somethings if the answer is wrong or right (see above for some ideas)

**Wonderful Resources**\
djaiss [mapsicon](https://github.com/djaiss/mapsicon).\
[Pytorch Computer Vision](https://www.learnpytorch.io/03_pytorch_computer_vision/)

