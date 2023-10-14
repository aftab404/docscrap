import streamlit as st



def main():
    st.set_page_config(page_title="DocScrapper", page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input(label="Ask a question :")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload PDFs here and click on 'Process'")
        st.button("Process")

if __name__ == '__main__':
    main()