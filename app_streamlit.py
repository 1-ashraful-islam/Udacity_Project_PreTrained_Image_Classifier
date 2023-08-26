# imports
import streamlit as st

# Imports classifier function for using CNN to classify images 
from classifier import classifier
from adjust_results4_isadog import adjust_results4_isadog


# use the streamlit app for showing the classification results in a web app
def app():
    st.title('Using a Pre-trained Image Classifier to Identify Dog Breeds')
    st.write('This is the classification results page of Udacity Project for AI Programming with Python Nanodegree.')

    # file name containing the dog names
    dogfile = 'dognames.txt'

    # make two columns to show hyperparameters and results
    col1, col2 = st.columns(2)

    with col1:
        # let the user choose the architecture to use
        architecture = st.radio('Choose the architecture to use:', ['VGG', 'AlexNet', 'ResNet'])
        # architecture = st.selectbox('Choose the architecture to use:', ['VGG', 'AlexNet', 'ResNet'])
        

        # allow the user to upload an image
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")

        # create a button to classify that is only enabled if the user uploaded an image
        classify_button = st.button('Classify', key='classify_button', disabled=uploaded_file is None, help='Upload an image to classify')
    
    # if the user clicked the classify button
    if classify_button:
        with col2:
            classifier_label = classifier(uploaded_file, architecture.lower()).lower().strip()
            st.write('**The classifier label is:** ' + classifier_label)

            # check if the classifier label is a dog
            # create a results dic with the file name as key and a list as value
            # the list contains the pet label, the classifier label, match/no match, dog/not dog, classifier dog/not dog
            # for this app we are going to only use the classifier label and the classifier dog/not dog
            results = dict()
            results[uploaded_file.name] = [uploaded_file.name, classifier_label, 0]
            adjust_results4_isadog(results, dogfile)

            # check if the classifier label is a dog
            if results[uploaded_file.name][4] == 1:
                st.write('**The classifier label:** is a dog')
            else:
                st.write('**The classifier label:** is not a dog')

            
            # show the image
            st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)



# run the app
if __name__ == '__main__':
    app()