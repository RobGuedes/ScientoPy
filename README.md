# ScientoPy

ScientoPy is a open-source Python based scientometric analysis tool.
It has the following main characteristics: 

 
- Import Clarivate Web of Science (WoS) and Scopus data set
- Filter publications by document type
- Merge WoS and Scopus data set based on a field tags correlation table
- Find and remove duplicated documents
- H-index extraction for the analyzed topics.
- Country and institution extraction from author affiliations
- Top authors, countries, or institutions based on first document's authors or all document's authors
- Preprocessing brief graph and report table
- Top topics and specific topics analysis
- Wildcard topics search
- Trending topics using the top average growth rate (AGR)
- Five different visualization graphs: bar, bar trends, timeline, evolution, and word cloud
- Graphical user interface


Installation
=============

1. Check instructions from: <https://github.com/jpruiz84/ScientoPy/releases>

2. Clone this repository.

**IMPORTANT NOTE:** This fork was made for ScientoPy to work with Python version 3.12.


## How to cite ScientoPy

If you use ScientoPy in a book, paper, website, technical report, etc., please include a reference to ScientoPy.

To cite ScientoPy, use the following [reference](https://link.springer.com/article/10.1007/s11192-019-03213-w):

> Ruiz-Rosero, J., Ramirez-Gonzalez, G., & Viveros-Delgado, J. (2019). Software survey: ScientoPy, a scientometric tool for topics trend analysis in scientific publications. Scientometrics, 1-24.

The bibtex entry for this is:

    @Article{Ruiz-Rosero2019,
        author="Ruiz-Rosero, Juan
        and Ramirez-Gonzalez, Gustavo
        and Viveros-Delgado, Jesus",
        title="Software survey: ScientoPy, a scientometric tool for topics trend analysis in scientific publications",
        journal="Scientometrics",
        year="2019",
        month="Nov",
        day="01",
        volume="121",
        number="2",
        pages="1165--1188",
        abstract="Bibliometric analysis is growing research filed supported in different tools. Some of these tools are based on network representation or thematic analysis. Despite years of tools development, still, there is the need to support merging information from different sources and enhancing longitudinal temporal analysis as part of trending topic evolution. We carried out a new scientometric open-source tool called ScientoPy and demonstrated it in a use case for the Internet of things topic. This tool contributes to merging problems from Scopus and Clarivate Web of Science sources, extracts and represents h-index for the analysis topic, and offers a set of possibilities for temporal analysis for authors, institutions, wildcards, and trending topics using four different visualizations options. This tool enables future bibliometric analysis in different emerging fields.",
        issn="1588-2861",
        doi="10.1007/s11192-019-03213-w",
        url="https://doi.org/10.1007/s11192-019-03213-w"
    }



## Authors

* **Juan Ruiz-Rosero** - *Initial work and documentation* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


