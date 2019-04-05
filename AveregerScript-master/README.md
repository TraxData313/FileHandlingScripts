<p><em>Disclaimer:</em></p>
<blockquote>
<p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>
</blockquote>

# Description:
- Gets file containing numerical values and outputs file with less entries, where each entry is an average of n entries of the input file

# Usage/Example:
- You have a file* containing the stock prices for a day for each minute, and you want a file containing the prices for each hour
- Download the "avereger.py" file to the dir containing the input file* and edin the avereger script to specify its name
- On the prompt "How much entries to average" enter 60 (as there are 60 minutes per hour)
- The averager will take the first 60 entries (60 minutes) of the input file, average them and set the result to the first entry of the output file (first 1 hour averaged). It will loop until the end of the input file, to produce the output file
- Output file lenght = Input file lenght / entries to average
