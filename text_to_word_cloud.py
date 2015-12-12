#! usr/bin/env python3
"""
This code prepares the cloud data in a format R can  read it  in
using read_table, for use by the R wordcloud package.

If R is installed and runnable as commandline program in batch mode,
run::

>>> save_il_to_word_cloud_file(word_cloud_file,word_counts_dict,vocab_size,call_R=True)

and R will be called to create the word cloud pdf file.
The font size arguments of C{save_il_to_word_cloud_file} often have to be tweaked.
They specify the size of the largest and smallest fonts in the word cloud.
The range of sizes may have to made smaller in order to get a healthy looking
roughly spherical word cloud to fit on a page.  The vocab size can also be
reduced to do this.

Otherwise::

  >>> save_il_to_word_cloud_file(word_cloud_file,word_counts_dict,vocab_size)

will just create a '.dat' file of the right sort for R to load.

Then the following R commands will create the .pdf file.

> require(wordcloud)
Loading required package: wordcloud
Loading required package: Rcpp
Loading required package: RColorBrewer
> mr = read.table("word_cloud.dat",header=TRUE)
> wordcloud(mr$Word,mr$Score,c(4,.3),2,,FALSE,,.15,pal)
> pal <- brewer.pal(9,"BuGn")
> pal <- pal[-(1:4)]
> wordcloud(mr$Word,mr$Score,c(4,.3),2,,FALSE,,.15,pal)

The expression "c(4,.3)" is an R vector which specifies the size of
the largest and smallest font.  As noted above,
that range of sizes often has to be tweaked in order
to make the word cloud words fit comfortably on the display
canvass.  The vocab size can also be reduced to do
this.

So for example for a vocab size of 500,

>wordcloud(mr$Word,mr$Score,c(6,.3),2,,FALSE,,.15,pal)

gives a good looking word cloud.
"""

#import codecs,os.path
import codecs, os.path, subprocess

########################################################################
########################################################################
###
###
###      W o r d          C l o u d         F i l e s
###
###
########################################################################
########################################################################

def save_il_to_word_cloud_file(word_cloud_file,int_scores_il,vocab_size,float_score=False,tagged=False,utf8=False,small_font_size=.3,large_font_size=7,call_R=False):
    """
    Use the item list C{int_scores_il} to print out 

    save this string in the file R_Batch_file
    If call_R = True, call R wordcloud package on wordcloud file
"""
    ctr = 0
    word_set = set()
    with open(word_cloud_file,'w') as ofh:
        print >> ofh, '"Word"   "Score"'
        for (i,w) in enumerate(int_scores_il):
            if i == vocab_size:
                break
            s=int_scores_il[w]
            if utf8:
               w = codecs.utf_8_encode(w)[0]
            if w in word_set:
                continue
            else:
                ctr += 1
                word_set.add(w)
                if float_score:
                    print >> ofh, '"%d" "%s" %.8f' % (ctr,w,s)
                else:
                    print >> ofh, '"%d" "%s" %d' % (ctr,w,s)
    if call_R:
        call_R_on_wordcloud_file (word_cloud_file,small_font_size,large_font_size)

def call_R_on_wordcloud_file (word_cloud_file,small_font_size,large_font_size):
    """
    This is a fairly clunky interface which creates an R batchfile
    using C{word_cloud_R_script_template}, then calls R to execute it.
    Parameters C{small_font_size} and C{large_font_size},
    the two most salient tweakables in getting a nice-looking word-cloud file,
    are passed into to the batchfile string.  To tweak other
    parameters (like color), you need to read the R docs for the
    word cloud package and edit the string C{word_cloud_R_script_template}
    to reflect your newfound wisdom.
    """
    
    (base,ext) = os.path.splitext(word_cloud_file)
    word_cloud_R_batch = base + '.R'
    with open(word_cloud_R_batch,'w') as ofh:
        print >> ofh, word_cloud_R_script_template % (word_cloud_file,base,large_font_size,small_font_size)
    print 'Calling R: %s' % ('R CMD BATCH %s' % (word_cloud_R_batch,),)
    #os.system('R CMD BATCH %s' % (word_cloud_R_batch,))
    os.system('Rscript {0}'.format(word_cloud_R_batch))
    #subprocess.call(['Rscript', word_cloud_R_batch], shell=True)

def map_to_int_scores(il):
    """
    C{il} is a sorted item list, whose keys are word-tag pairs,
    whose values are mi-numbers (floats in general).
    
    To map mi values to ints, multiply all
    values in the set by a constant that makes the smallest
    exactly equal to 1. Round off other results. Yukky
    but roughly right.
    """
    ((w,t),lowest) = il[-1]
    factor = float(1)/lowest
    return (((w,t), int(math.ceil(factor * s))) for ((w,t),s) in il)


    
word_cloud_R_script_template = \
"""
require(wordcloud)
mr = read.table('%s',header=TRUE)
pal <- brewer.pal(9,"BuGn")
pal <- pal[-(1:4)]
pdf('%s.pdf')
wordcloud(mr$Word,mr$Score,c(%s,%s),2,,FALSE,,.15,pal)
"""
