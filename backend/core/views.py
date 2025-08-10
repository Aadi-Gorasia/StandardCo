# core/views.py

from django.shortcuts import render

# --- View for the Homepage ---
def homepage(request):
    """ Renders the main homepage. """
    return render(request, 'core/homepage.html')


# --- View for the About Us Page ---
def about_page(request):
    """ Renders the "About Us" page for the "Standard" theme. """
    founders = [
        {
            'name': 'gorastax',
            'role': 'Founder & Chief Architect',
            'bio': 'The visionary force behind the Standard engine. Driven by a frustration with bloated, restrictive tools, he architected a system that puts raw creative power back into the hands of the user.',
            'image_url': 'https://i.pravatar.cc/500?u=gorastax'
        },
        {
            'name': 'Laukik',
            'role': 'Co-Founder & Lead Strategist',
            'bio': 'The master planner who tempers raw power with purpose. He ensures every feature and design choice serves the ultimate mission: empowering creators to build their legacy.',
            'image_url': 'https://i.pravatar.cc/500?u=laukik'
        }
    ]
    principles = [
        { 'name': 'Radical Ownership', 'description': 'Your creation is yours. We provide the tools, but you own every line of code. No lock-ins, no walled gardens, ever.' },
        { 'name': 'Power in Simplicity', 'description': 'True power isn’t about endless features; it’s about the perfect tool for the job. We obsessively refine our engine to be powerful, not complicated.' },
        { 'name': 'Design as a Statement', 'description': 'A website is more than information. It’s an identity. We believe in building digital presences that are bold, intentional, and unforgettable.' }
    ]
    context = {
        'founders': founders,
        'principles': principles
    }
    return render(request, 'core/about.html', context)


# --- View for the Contact Page ---
def contact_page(request):
    """ Renders the contact page. """
    return render(request, 'core/contact.html')


# --- View for the Features Page ---
def features_page(request):
    """ Renders the features page and passes detailed information. """
    features = [
        {
            'name': 'AI-Powered Assistant',
            'description': 'Our integrated AI is more than a chatbot. It acts as your co-pilot, helping you generate compelling branding copy, suggesting effective page layouts, and refining your message to ensure your site is both beautiful and impactful from the moment you start building.',
            'sub_points': ['Intelligent copy generation', 'Layout and structure suggestions', 'Real-time design feedback'],
            'svg_icon_path': '<path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z" />'
        },
        {
            'name': 'Blazing Fast Generation',
            'description': 'Time is your most valuable asset. The Standard engine is engineered for pure speed, compiling your inputs and chosen blueprint into a complete, deployment-ready website in seconds, not hours. We handle the complexity so you can focus on creativity.',
            'sub_points': ['Instantaneous site compilation', 'Optimized for global performance', 'Zero-config deployment'],
            'svg_icon_path': '<path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" />'
        },
        {
            'name': 'Radical Code Ownership',
            'description': 'We believe in empowerment, not entrapment. At any point, you can download a clean, human-readable ZIP file of your website’s complete source code. No proprietary formats, no vendor lock-in. Your creation is truly yours, forever.',
            'sub_points': ['Clean HTML, CSS, and JS', 'No platform dependencies', 'Host anywhere, modify anytime'],
            'svg_icon_path': '<path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />'
        }
    ]
    context = {
        'features': features
    }
    return render(request, 'core/features.html', context)


# --- View for the Donate Page ---
def donate_page(request):
    """
    Renders the simple, clean donate page.
    """
    return render(request, 'core/donate.html')