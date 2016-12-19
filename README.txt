### Assigment3: Topic modelling software ###

Toolkit: GibbsLDA++: A C/C++ Implementation of Latent Dirichlet Allocation
Copyright © 2007-2008 by Xuan-Hieu Phan and Cam-Tu Nguyen
url: http://gibbslda.sourceforge.net/

GibbsLDA++ is a C/C++ implementation of Latent Dirichlet Allocation (LDA) using Gibbs Sampling technique for parameter estimation and inference. It is very fast and is designed to analyze hidden/latent topic structures of large-scale datasets including large collections of text/Web documents. LDA was first introduced by David Blei et al [Blei03]. There have been several implementations of this model in C (using Variational Methods), Java, and Matlab. We decided to release this implementation of LDA in C/C++ using Gibbs Sampling to provide an alternative to the topic-model community.

GibbsLDA++ is useful for the following potential application areas:

Information retrieval and search (analyzing semantic/latent topic/concept structures of large text collection for a more intelligent information search).
Document classification/clustering, document summarization, and text/web mining community in general.
Content-based image clustering, object recognition, and other applications of computer vision in general.
Other potential applications in biological data.
Contact us: all comments, suggestions, and bug reports are highly appreciated. And if you have any further problems, please contact us:

Xuan-Hieu Phan (pxhieu at gmail dot com), was at Tohoku University, Japan (now at Vietnam National University, Hanoi)
Cam-Tu Nguyen (ncamtu at gmail dot com), was at Vietnam National University, Hanoi (now at Google Japan)

License: GibbsLDA++ is a free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. GibbsLDA++ is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with GibbsLDA++; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.

** Example **
Input: Reuters
Output: test_docs.dat, train_docs.dat
# python create_data.py
Copy 'test_docs.dat', 'train_docs.dat' to GibbsLDA++-0.2/models/demo/
# cp test_docs.dat GibbsLDA++-0.2/models/demo/
# cp train_docs.dat GibbsLDA++-0.2/models/demo/
Running topic modeling
We want to estimate for 10 topics with alpha = 0.5 and beta = 0.1. We want to perform 1000 Gibbs sampling iterations, save a model at every 100 iterations, and each time a model is saved, print out the list of 100 most likely words for each topic. Supposing that we are now at the home directory of GibbsLDA++, We will execute the following command to estimate LDA model from scratch:
# cd GibbsLDA++-0.2/
Input: train_docs.dat
Output: model, word_map.txt
# src/lda -est -alpha 0.5 -beta 0.1 -ntopics 10 -niters 1000 -savestep 200 -twords 100 -dfile models/demo/train_docs.dat

Now, look into the demo directory, we can see the outputs of the inferences:
	model-final.others
	model-final.phi
	model-final.tassign
	model-final.theta
	model-final.tword



