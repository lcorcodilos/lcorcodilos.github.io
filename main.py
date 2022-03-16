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
                    '''I am a data scientist with experience analyzing large data sets, writing internal software
                    tools, and advising teams on statistical models and software in the field of experimental particle physics.''',
                    '''I wrote the HTML and CSS for this site so if there are bugs or typos, please let me know!'''
                ]),
                Bullets(
                    header='I have experience in:',
                    items=[
                        'Cleaning, analyzing, and interpreting large datasets with Python-based tools.',
                        'Advising research teams on statistical modeling choices and testing.',
                        'Developing Python packages to automate and standardize data manipulations for teams.',
                        'Creating Django-based web applications and deploying to AWS Elastic Beanstalk.',
                        'Using GitHub workflows + Docker for CI/CD that automates testing, compiling, and deployment of projects.',
                        'Giving technical presentations to group leaders and general talks at conferences with 100s of attendees',
                        'Performing and publishing rigorous scientific research based on analysis of large datasets.',
                    ]
                ),
                Bullets(
                    header='Principles that guide my work:',
                    items=[
                        'Data insights are most interesting for <span style="font-style: italic;">developing</span> products, not marketing them.',
                        'A product is only as good as its user interface.',
                        'Jupyter Notebooks have very little use outside of 15 min windows of EDA<span style="font-style: italic;">(I may upset some people with that one...)</span>.'
                    ]
                ),
                Dropdown(
                    ID='HEP', header='A breakdown of my work in particle physics',
                    items=[
                        Bullets(
                            header='',
                            items=[
                                '''I have published independent research performed with data collected by
                                the Compact Muon Solenoid (CMS) experiment, an international
                                collaboration made up of thousands of researchers.''',
                                '''My analysis increased the sensitivity to detect a specific particle decay by a factor of 10x.
                                The result has been accepted by the Journal of High Energy Physics and is publicly available at
                                <a href="https://arxiv.org/abs/2104.12853">arXiv:2104.12853</a>. I also helped draft a
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
            ID='projects', classname='', header='Projects',
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
                            '''TIMBER (Tree Interface for Making Binned Events with RDataFrame) is an easy-to-use library of python and C++ tools that can
                            quickly process CMS data sets with RDataFrame. Default arguments assume the use of the NanoAOD format but
                            any ROOT TTree can be processed along with other RDataFrame-supported data formats.''',
                            '''While TIMBER provides a library of C++ modules that implement common CMS analysis algorithms, the main
                            python class is used to track the dataframe processing "tree" and to leverage the information in the tree 
                            to automate otherwise tedious and error-prone tasks.'''
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
                            ''' A user-friendly framework that constructs a domain specific two-dimensional
                            model, fits it to data via a maximum likelihood estimate, and collects the 
                            fit result and plots the results.''',
                            '''The model simultaneously estimates combinatorial backgrounds from data
                            in a control region while morphing background and signal simulation shape templates.
                            It can also perform basic manipulation of input histograms and automatically
                            produces a suite of plots comparing the total background model to data in projections,
                            comparing pre-fit and post-fit background components, and more.'''
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
                            '''Tool to automate the various processing steps to generate Fast Simulation
                            and to validate across FastSim versions (in particular for when changes need
                            to be actively tested). Despite the name, this tool can be used outside of
                            tracking validation since the main infrastructure is in automating the consecutive
                            processing steps and the submissions to the CRAB batch system. It is also "smart enough" to wait for CRAB to 
                            finish before proceeding. The package also congregates existing tools to run comparisons
                            across simulated samples.'''
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
                            '''Simple tool to batch track CRAB jobs on CMS using the CRABClient API. Skips checking
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
                        '''During the COVID-19 pandemic, voluneered as a tutor for two high
                        school students taking AP Physics remotely.''',
                        '''For 2.5 years, served as a revision-based writing tutor at the Rutgers
                        Plangere Writing Center.'''
                    ])
                ]
            ),
            Project(
                ID='TA', header='Teaching Assitant',
                subheader='Early 2018 - Fall 2021',  #image='images/jhu.png',
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
                    'Python, C++, HTML, CSS, LaTeX, ROOT',
                    'Linux, Git, Doxygen, Jekyll', 
                    'GitHub Actions, Docker, AWS'
                ]),
                ('Packages', [
                    'Pandas, Plotly/Dash, scikit-learn, Keras',
                    'Django, Jinja, Beautiful Soup, Pytest' 
                ]),
                ('Techniques', [
                    'Statistical/ML modeling, web scraping',
                    'Distributed computing, multi-processing',
                    'User support'
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