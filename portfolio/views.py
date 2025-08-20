from django.shortcuts import render

def home(request):
    """Home view for the personal portfolio."""
    context = {
        'name': 'Zhang Yanbo',
        'phone': '13857103550',
        'email': '3200104883@zju.edu.cn',
        'education': [
            {
                'university': 'Duke University',
                'degree': 'Master of Science in Computer Engineering',
                'school': 'Pratt School of Engineering',
                'location': 'Durham, North Carolina, USA',
                'gpa': '3.85/4.0',
                'period': '2024.08 - 2026.05'
            },
            {
                'university': 'Zhejiang University',
                'degree': 'Bachelor of Engineering in Electrical Engineering and Automation',
                'school': 'School of Electrical Engineering',
                'location': 'Hangzhou, Zhejiang, China',
                'gpa': '3.81/4.0',
                'period': '2020.09 - 2024.06'
            }
        ],
        'experience': [
            {
                'company': 'Alibaba Group',
                'position': 'Intern Software Engineer',
                'department': 'Youku',
                'period': '2025.05 - 2025.08'
            },
            {
                'company': 'Chinese University of Hong Kong',
                'position': 'Research Assistant',
                'department': 'Cybersecurity Laboratory',
                'period': '2023.07 - 2023.10'
            }
        ]
    }
    return render(request, 'portfolio/home.html', context) 