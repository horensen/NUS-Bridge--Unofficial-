from nltk.corpus import wordnet

class SemanticTest(webapp2.RequestHandler):
    def get(self):
        #word1 = 'animal'
        #word2 = 'organism'
        #sm = SequenceMatcher(None)
        #sm.set_seq1(word1)
        #sm.set_seq2(word2)
        #sequence_similarity_ratio = '{0:.0%}'.format(sm.ratio())
        #sequence_matcher_result = word1 + " and " + word2 + " are " + sequence_similarity_ratio + " similar in spelling."
        
        #  -------------------------------------------- ----------------------------------------------------
        # These are working in the Terminal or Command Prompt
        #set1 = wordnet.synset('animal.n.01')
        #set2 = wordnet.synset('organism.n.01')
        #wup_similarity_ratio = set1.wup_similarity(set2) # Wu-Palmer Similarity
        #wup_similarity_result = "animal and organism are " + wup_similarity_ratio + " similar in meaning."
        # --------------------------------------------------------------------------------------------------

        #wordx, wordy = "cat","dog"
        #sem1, sem2 = wn.synsets(wordx), wn.synsets(wordy)
        #maxscore = 0
        #for i,j in list(product(*[sem1,sem2])):
        #    score = i.wup_similarity(j) # Wu-Palmer Similarity
        #    maxscore = score if maxscore < score else maxscore

        template_values = {
            #'sequence_matcher_result': sequence_matcher_result,
            'wup_similarity_result': wup_similarity_result
        }
        template = jinja_environment.get_template('semantictest.html')
        self.response.out.write(template.render(template_values))