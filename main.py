from jinja2 import Environment, FileSystemLoader
from dataclasses import dataclass, field
from typing import List, Dict, Union, Tuple

def render_template(in_name, outname, include_path=['templates','include'], **kwargs):
    post = Environment(loader=FileSystemLoader(include_path)).from_string(open(in_name).read())

    out = post.render(kwargs)
    with open(outname,'w') as rendered:
        rendered.write(out)

'''---------------Base pieces---------------'''
@dataclass(kw_only=True)
class HTML:
    classname: str
    ID: str

@dataclass(kw_only=True)
class P(HTML):
    ID: str = ''
    classname: str = 'p'
    header: str = ''
    items: List[str]

@dataclass(kw_only=True)
class Bullets(HTML):
    ID: str = ''
    classname: str = 'bullets'
    header: str = ''
    items: List[str]

@dataclass(kw_only=True)
class Dropdown(HTML):
    classname: str = 'expander'
    header: str
    items: List[Union[P, Bullets]]

'''-----------------Card pieces---------------'''
@dataclass(kw_only=True)
class Card(HTML):
    header: str

@dataclass(kw_only=True)
class Profile(Card):
    classname: str = 'profile'
    ID: str = 'profile'

    image: str
    titles: List[str]
    social_links: Dict[str, str]
    
@dataclass(kw_only=True)
class Education(Card):
    classname: str = 'edu'
    ID: str = 'edu'
    header: str = 'Education'

    schools: List[Dict[str, Union[str, List[str]]]]

@dataclass(kw_only=True)
class Skills(Card):
    classname: str = 'skills'
    ID: str = 'skills'
    
    skills: List[ Tuple[str, List[str]]]

@dataclass(kw_only=True)
class BodyCard(Card):
    classname: str = 'body'
    
    content: List[Union[P, Bullets, Dropdown]]

'''---------------Project pieces---------------'''
@dataclass(kw_only=True)
class Project(Dropdown):
    classname: str = 'project'
    subheader: str
    image: str = ''
    links: List[Tuple[str, str]] = field(default_factory=list)

if __name__ == '__main__':
    welcome_card = BodyCard(
            ID='welcome', classname='', header='Welcome!',
            content=[
                P(items=[
                    '''I am a data scientist with experience analyzing large data sets, working with unbalanced data,
                    designing streaming applications, and building custom purpose-driven models. I currently work in cybersecurity
                    at Vectra AI and formerly worked in experimental particle physics as a part of the CMS Collaboration.''',
                    '''I wrote the HTML and CSS for this site so if there are bugs or typos, please let me know!'''
                ]),
                Bullets(
                    header='I have experience in:',
                    items=[
                        'Working with streaming data in the context of developing real time cyber attacker detection algorithms.',
                        'Analyzing unbalanced datasets, specifically in cybersecurity where malicious samples are hard to come by.',
                        'Standard python coding practices including Black formatting, type hinting, and unit testing.',
                        'Source code management via git including using GitHub workflows + Docker for CI/CD that automates testing, compiling, and deployment of projects.',
                        'Developing Python packages to improve workflows for myself and others on my team, including using Docker to build services that support development work.',
                        'Investigating customer issues in on-prem and cloud environments, working with support teams to address customer concerns.',
                        'Following the latest developments on large language model (LLM) research.',
                        'Giving presentations on technical topics in various forums ranging from rooms of engineers to company leadership to conference attendees.',
                        'Performing and publishing rigorous scientific research.',
                    ]
                ),
                Bullets(
                    header='Principles that guide my work:',
                    items=[
                        'Data insights are most interesting for <span style="font-style: italic;">developing</span> products, not marketing them.',
                        'A product is only as good as its user experience.',
                        'Jupyter Notebooks should be limited to 15 min windows of EDA <span style="font-style: italic;">(I may upset some people with that one...)</span>.'
                    ]
                ),
                Dropdown(
                    ID='Vectra', header='My work at Vectra AI',
                    items=[
                        Bullets(
                            header='',
                            items=[
                                '''I've worked on detection algorithms in both network and cloud environments (AWS and M365 specifically).''',
                                '''On the network side, I've developed algorithms to detect DCSync and DCShadow attacks via the DRSUAPI. I've also worked on
                                logic to detect reconnaissance activity via LDAP.''',
                                '''On the cloud side, I've worked on algorithms that detect suspicious SharePoint downloading activity as well
                                as recon in AWS environments from credentials stolen from insecure EC2 instances.''',
                                '''I've also participated in efforts to understand the underlying behavior of Command-and-Control channels.''',
                                '''As a part of a small team, I investigated using LLMs in the product's interface. I've investigated the feasibility
                                of Natural Language to SQL query systems and the potential for fine-tuning open source models via methods such as LoRA and QLoRA.
                                For this work, I also built an ORM-based package for defining, running, and visualizing repeatable experiments on LLMs
                                and prompts for LLMs.''',
                            ]
                        )
                    ]
                ),
                Dropdown(
                    ID='HEP', header='My work in particle physics',
                    items=[
                        Bullets(
                            header='',
                            items=[
                                '''I published independent research performed with data collected by
                                the Compact Muon Solenoid (CMS) experiment, an international
                                collaboration made up of thousands of researchers.''',
                                '''My analysis increased the sensitivity to detect a specific particle decay by a factor of 10x.
                                The result was published by the Journal of High Energy Physics and is publicly available at
                                <a href="https://arxiv.org/abs/2104.12853">arXiv:2104.12853</a>. I also helped draft
                                a CMS Physics Briefing for the analysis as a way to highlight my work to the public.
                                It can be found <a href="https://cms.cern/news/getting-excited-about-quarks">here</a>.''',
                                '''I created and developed two software tools (TIMBER and 2DAlphabet) that
                                provide fast, user-friendly python interfaces to commonly used tools,
                                algorithms, and statistical models used in particle physics.''',
                                '''I completed a two year tenure as the designated statistics software expert for a group of
                                40-60 people where I was responsible for approving statistical models and their software implementation
                                for 10-15 different analyses per year.'''
                            ]
                        )
                    ]
                )
            ]
        )

    project_card = BodyCard(
            ID='projects', classname='', header='Old Projects',
            content=[
                Project(
                    ID='TIMBER', header='TIMBER', subheader='Creator, Lead Developer',
                    image='https://raw.githubusercontent.com/lcorcodilos/TIMBER/master/doxysetup/logo_clear.png',
                    links=[
                        ('Documentation', 'https://lcorcodilos.github.io/TIMBER/'),
                        ('Source code', 'https://github.com/lcorcodilos/TIMBER')
                    ],
                    items=[
                        P(items=[
                            '''TIMBER (Tree Interface for Making Binned Events with RDataFrame) is an easy-to-use Python library 
                            that can quickly process CMS datasets with plug-and-play C++ modules, reducing computation
                            time by up to a factor of 20x.''',
                            '''The primary class builds a directed acyclic graph (the "tree") from successive data manipulations so
                            internal methods can leverage data provenance.'''
                            '''The interface makes analysis development quicker and encourages better coding praxis so that
                            analysis code can be more easily shared and understood.'''
                        ])
                    ]
                ),
                Project(
                    ID='2DAlpha', header='2D Alphabet', subheader='Creator, Lead Developer',
                    links=[
                        ('Documentation', 'https://lcorcodilos.github.io/2DAlphabet/'),
                        ('Source code', 'https://github.com/lcorcodilos/2DAlphabet')
                    ],
                    items=[
                        P(items=[
                            '''The software implementation of the novel modeling technique I developed
                            of the same name, 2D Alphabet constructs a binned likelihood from 2D parametric
                            distributions constrained by simulation. Built in methods can also fit
                            and test the model and produce publication-ready figures of the post-fit results.''',
                            '''The exposed API also allows for custom models to be built from the fundamental pieces
                            of the 2D Alphabet framework.'''
                        ])
                    ]
                ),
                Project(
                    ID='JAM', header='Job Application Manager', subheader='Creator, Lead Developer',
                    links=[
                        # ('Website', 'https://jobs.lucascorcodilos.com'),
                        # ('Source code', 'https://github.com/lcorcodilos/TIMBER')
                    ],
                    items=[
                        P(items=[
                            '''An online tool to track and manage job applications and interviews.
                            Stores dates/times, notes, resume version, and other information with sort and filter
                            functionality to make it easier to track 100s of job applications.''',
                            '''Developed in Django and deployed with AWS Elastic Beanstalk (EOL: April 2023).'''
                        ])
                    ]
                ),
                Project(
                    ID='ROOT', header='Better ROOT Browser', subheader='Creator, Lead Developer',
                    # image='https://raw.githubusercontent.com/lcorcodilos/TIMBER/master/doxysetup/logo_clear.png',
                    links=[
                        ('<i>In progress</i>', '#'),
                        # ('Source code', 'https://github.com/lcorcodilos/TIMBER')
                    ],
                    items=[
                        P(items=[
                            '''A Dash web-application which uses Plotly to provide an interactive interface
                            for browsing ROOT files.''',
                            '''In addition to basic browsing functionality similar to ROOT's TBrowser, Better ROOT
                            Browser includes utilities, such as the template morphing sliders, that make EDA tasks interactive.'''
                        ])
                    ]
                ),
                Project(
                    ID='FSVT', header='FastSim Validation Tool', subheader='Creator',
                    links=[
                        ('Source code', 'https://github.com/lcorcodilos/FastSimTrackingValidation')
                    ],
                    items=[
                        P(items=[
                            '''Tool to automate the various processing steps to generate CMS Fast Simulation
                            and to validate across FastSim versions (in particular for when changes need
                            to be actively tested). The main infrastructure is in automating the consecutive
                            processing steps and the submissions to the CRAB batch system. The tool will wait for CRAB to 
                            finish processing jobs before proceeding to subsequent steps.
                            The package also congregates existing tools to create comparisons across simulation samples.'''
                        ])
                    ]
                ),
                Project(
                    ID='CRAB', header='CRAB Task Tracker', subheader='Creator',
                    links=[
                        ('Source code', 'https://github.com/lcorcodilos/CRABTaskTracker')
                    ],
                    items=[
                        P(items=[
                            '''Simple tool to batch track CRAB jobs using the CRABClient API. Skips checking
                            any jobs that are fully completed and makes recommendations to resubmit with more memory
                            if logs indicate this could help.'''
                        ])
                    ]
                ),
            ]
        )

    teaching_card = BodyCard(
        ID='teaching', classname='', header='Other Experiences',
        content=[
            Project(
                ID='publications', header='Publications', subheader='',
                items=[
                    Bullets(
                        header='Primary Author',
                        items=[
                                '''"Search for a heavy resonance decaying to a top quark and a
                                W boson at &radic;s = 13 TeV in the fully hadronic final state,"
                                CMS Collaboration, JHEP, 2021''',
                    ]),
                    Bullets(
                        header='Collaborator',
                        items=[
                                '''"Search for a heavy resonance decaying into a top quark and a
                                W boson in the lepton+jets final state at &radic;s = 13 TeV,"
                                CMS Collaboration, JHEP, 2022''',
                                '''"Search for a massive scalar resonance decaying to a light
                                scalar and a Higgs boson in the four b quarks final state with
                                boosted topology," Phys. Lett. B (2023)''',
                    ])
                ]
            ),
            Project(
                ID='conferences', header='Conference Oral Presentations', subheader='',
                items=[
                    Bullets(
                        header='"Search for heavy BSM particles coupling to third generation quarks at CMS"',
                        items=[
                                'SUSY Conference, <i>Spring 2019</i>',
                                'PHENO Conference, <i>Spring 2019</i>',
                                'Lake Louise Winter Institute, <i>Early 2019</i>'
                    ]),
                    Bullets(
                        header='"A search for an excited bottom quark decaying to a top quark and W boson in pp collisions at <math><msqrt><mi>s</mi></msqrt></math> = 13 TeV"',
                        items=[
                                'American Physical Society (APS), <i>April 2018</i>'
                    ])
                ]
            ),
            Project(
                ID='DAS', header='Data Analysis School Facilitator',
                subheader='Fall 2020, Early 2021', #image='images/cms.png',
                items=[
                    P(items=[
                        '''Helped to lead a week-long group exercise where students new to CMS data analysis
                        worked together to recreate my analysis. Helped to edit and provide approachable python code, gave presentations explaining
                        key statistics concepts, and answered student questions throughout the week. My group
                        from the 2021 session won best analysis!'''
                    ])
                ]
            ),
            Project(
                ID='outreach', header='Physics Outreach with Virtual Reality',
                subheader='Spring 2018, 2019', #image='images/jhu.png',
                items=[
                    Bullets(items=[
                        '''Using personal hardware (PC + HTC Vive), provided a virtual reality
                        exhibit at the annual JHU Physics Fair which is free and open to the
                        Baltimore community to enjoy.''',
                        '''In 2018, the experience gave visitors
                        a tour of the ATLAS detector at the LHC via <a href="https://inspirehep.net/literature/1402327)" style="text-decoration: underline;">ATLASrift</a>.''',
                        '''In 2019, the experience allowed
                        visitors to step "inside" the Belle II detector at the SuperKEKB accelerator
                        to watch slow motion electron-positron collisions and the particle showers 
                        that result via <a href="http://www1.phys.vt.edu/~piilonen/VR/" style="text-decoration: underline;">Belle II VR</a>.'''
                    ]),
                ]
            ),
            Project(
                ID='tutor', header='Tutor',
                subheader='',
                items=[
                    Bullets(items=[
                        '''Volunteered as a tutor for high
                        school AP Physics students struggling with remote schooling during the COVID-19 pandemic.''',
                        '''Served as a revision-based writing tutor at the Rutgers
                        Plangere Writing Center for 2.5 years.'''
                    ])
                ]
            ),
            Project(
                ID='TA', header='Teaching Assitant',
                subheader='',  #image='images/jhu.png',
                items=[
                    Bullets(
                        header='Classical Mechanics (Freshman physics majors)',
                        items=['Every Fall from 2017 to 2020']
                    ),
                    Bullets(
                        header='General Physics Lecture and Lab',
                        items=['Fall 2016, Spring 2017']
                    )
                ]
            ),
            Project(
                ID='mentor', header='Mentor',
                subheader='Early 2018 - Fall 2021',
                items=[
                    P(items=[
                        '''Mentored both undergraduate and graduate students in their pursuits
                        to begin research in the JHU experimental particle physics group.
                        Assisted with a variety of topics ranging across physics concepts, 
                        coding tools, and statistical analysis.'''
                    ])
                ]
            )
        ]
    )

    sidecards = [
        Profile(
            header='Lucas Corcodilos',
            image='images/Lucas_Corcodilos_small.jpg',
            titles=[
                'Data Scientist',
                'Ph.D. Experimental Particle Physics',
                'Former CMS Collaboration Member'
            ],
            social_links={
                'emails':'mailto:corcodilos.lucas@gmail.com',
                'github': 'https://github.com/lcorcodilos',
                'twitter': 'https://twitter.com/LucasCorcodilos'
            }
        ),
        Education(
            schools=[
                {
                    'logo': 'images/jhu.png',
                    'logo_class': 'jhu',
                    'name': 'Johns Hopkins University',
                    'time': 'Sept 2016 - Dec 2021',
                    'degrees': ['Ph.D. Experimental Particle Physics', 'M.S. Physics']
                },
                {
                    'logo': 'images/ru.png',
                    'logo_class': '',
                    'name': 'Rutgers University',
                    'time': 'Sept 2012 - May 2016',
                    'degrees': ['B.S. Physics', 'Minor Mathematics']
                }
            ]
        ),
        Skills(
            header='Technical Skills',
            skills=[
                ('Languages + Tools', [
                    'Python, C++, HTML, CSS',
                    'Linux, Git, Docker',
                    'Memgraph/Neo4j/Cypher',
                    'LaTeX, Doxygen, Jekyll',
                    'GitHub Actions, Docker, AWS'
                ]),
                ('Packages', [
                    'Pyspark, Polars, Numpy, Scipy, Pandas',
                    'Scikit-learn, Pytorch'
                    'Black, mypy, Pytest',
                    'Plotly/Dash',
                    'Django, Jinja, Beautiful Soup',
                ]),
                ('Techniques', [
                    'Statistical and ML modeling',
                    'Algorithm design',
                    'Source code management',
                    'Code review',
                    'Web scraping',
                    'Distributed computing, multi-processing',
                ])
            ]
        )
    ]

    bodycards = [
        welcome_card,
        project_card,
        teaching_card
    ]

    render_template('main.html', 'index.html', sidecards=sidecards, bodycards=bodycards)
