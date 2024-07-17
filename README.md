# Topic Modeling

This project implements Gibbs sampling inference for LDA (Latent Dirichlet Allocation).

## To-do
- Check convergence
- Speed up Gibbs sampling process

## Reference
- Heinrich, G. (2005). Parameter estimation for text analysis. [Link](http://www.arbylon.net/publications/text-est.pdf)

## How to Run
To run the project, use the following command:
```bash
python main.py <number_of_topics> <alpha> <beta> <max_iterations>
```
### Parameters

- `<number_of_topics>`: Number of topics to infer from the corpus.
- `<alpha>`: Dirichlet parameter for document-topic distributions.
- `<beta>`: Dirichlet parameter for topic-word distributions.
- `<max_iterations>`: Maximum number of iterations for Gibbs sampling.

## Notes
- Gibbs sampling can be slow, and checking convergence is challenging.
- Results may vary due to corpus size and other factors.
- Results can differ significantly across different runs.

## Topic Modeling Tools
- [David Blei's collection](http://www.cs.princeton.edu/~blei/topicmodeling.html)
- [Mallet from UMass](http://mallet.cs.umass.edu/)
- [Stanford Topic Modeling Toolbox](http://nlp.stanford.edu/software/tmt/tmt-0.4/)
- [Matlab Topic Modeling Toolbox by Mark Steyvers and Tom Griffiths](http://psiexp.ss.uci.edu/research/programs_data/toolbox.htm)
- [LDA-J](http://www.arbylon.net/projects/)
- R package: [topicmodels](http://cran.r-project.org/web/packages/topicmodels/vignettes/topicmodels.pdf) and [Topic models in R](http://cran.uvigo.es/web/packages/topicmodels/vignettes/topicmodels.pdf)
- [topic-modeling-tool](http://code.google.com/p/topic-modeling-tool/) (A graphical user interface tool based on Mallet)