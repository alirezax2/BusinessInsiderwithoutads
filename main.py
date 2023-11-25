
def return_buisnessinsider_withoutads(URL):
  import requests
  from bs4 import BeautifulSoup
  r= requests.get(URL)
  html_content = r.content.decode('utf-8')

  # Use BeautifulSoup to parse the HTML
  soup = BeautifulSoup(html_content, 'html.parser')

  # Find the div tag with class "content-lock-content"
  div_tag = soup.find('div', class_='content-lock-content')

  # Check if the div tag is found
  if div_tag:
      # Extract text content from the div tag
      text_content = div_tag.get_text(separator='\n', strip=True)

      # Print the extracted text content
      return f"{text_content}"
  else:
      return "Div tag with class 'content-lock-content' not found."


#Main  
import panel as pn

URL = "https://www.businessinsider.com/chatgpt-trading-stocks-high-returns-simulated-study-prompt-used-2023-7?r=US&IR=T"

text_input = pn.widgets.TextInput(name='BusinessInsider URL', value=URL , placeholder='Enter Business insdier URL here...')

button = pn.widgets.Button(name='Click me', button_type='primary')

pn.config.sizing_mode = 'stretch_height'
# pn.config.sizing_mode = 'stretch_width'
# TXT = return_buisnessinsider_withoutads(text_input.value)

pn.extension('texteditor')
pn.config.sizing_mode = 'stretch_width'

def return_editor(textinput):
  TXT = return_buisnessinsider_withoutads(textinput)
  return pn.widgets.TextEditor(value = TXT , toolbar=[
    ['bold', 'italic', 'underline', 'strike'],        # toggled buttons
    ['blockquote', 'code-block'],

    [{ 'header': 1 }, { 'header': 2 }],               # custom button values
    [{ 'list': 'ordered'}, { 'list': 'bullet' }],
    [{ 'script': 'sub'}, { 'script': 'super' }],      # superscript/subscript
    [{ 'indent': '-1'}, { 'indent': '+1' }],          # outdent/indent
    [{ 'direction': 'rtl' }],                         # text direction

    [{ 'size': ['small', False, 'large', 'huge'] }],  # custom dropdown
    [{ 'header': [1, 2, 3, 4, 5, 6, False] }],

    [{ 'color': [] }, { 'background': [] }],          # dropdown with defaults from theme
    [{ 'font': [] }],
    [{ 'align': [] }],

    ['clean']                                         # remove formatting button
  ] , sizing_mode='stretch_height')


pn.Column(
    text_input,button,
    pn.bind(return_editor , text_input)
).servable(title="Get BusinessInsider Article")