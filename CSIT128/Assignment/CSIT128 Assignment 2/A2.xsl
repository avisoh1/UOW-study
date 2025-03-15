<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml">

  <xsl:output method="html" indent="yes" encoding="UTF-8"/>

  <xsl:template match="/forecast">
    <html>
      <head> 
        <title>a2p3</title> 
        <style>
          .container {
            width: 70%;
            margin: auto;
            padding: 20px;
          }

           

          th {
            width: 90px;
            font-size: 15pt;
            height: 1px;
          } 

          td {
            width: 150px; /* Each column takes equal width */
            height: 150px; /* Fixed height for all cells */
            text-align: center; /* Center align text and images */
            vertical-align: middle; /* Center align content vertically */
            font-size: 15pt;
          }   

        </style>
      </head>

      <body>
        <div class="container">

          <h1><xsl:value-of select="@queryLocation" /> [<xsl:value-of select="@queryTime" />] </h1>
          
          <table border="1">
            <tr bgcolor="Aqua">
              <th>Date</th>
              <th>Mon</th>
              <th>Tue</th>
              <th>Wed</th>
              <th>Thu</th>
              <th>Fri</th>
              <th>Sat</th>
              <th>Sun</th>
            </tr>

            <xsl:for-each select="weather">
              <xsl:sort select="month" data-type="number" order="descending"/> <!--*sort by month -->
              <xsl:sort select="date" data-type="number" order="descending"/> <!--*sort by date -->

              <tr style="text-align:center">
                <td bgcolor="Aqua" style="width:40px;">
                  <xsl:value-of select="date"/>
                  <xsl:text> </xsl:text> 
                  <xsl:choose>
                    <xsl:when test="month = '1'">Jan</xsl:when>

                    <xsl:when test="month = '2'">Feb</xsl:when>

                    <xsl:when test="month = '3'">Mar</xsl:when>

                    <xsl:when test="month = '4'">Apr</xsl:when>

                    <xsl:when test="month = '5'">May</xsl:when>

                    <xsl:when test="month = '6'">Jun</xsl:when>

                    <xsl:when test="month = '7'">Jul</xsl:when>

                    <xsl:when test="month = '8'">Aug</xsl:when>

                    <xsl:when test="month = '9'">Sep</xsl:when>

                    <xsl:when test="month = '10'">Oct</xsl:when>

                    <xsl:when test="month = '11'">Nov</xsl:when>

                    <xsl:when test="month = '12'">Dec</xsl:when>
                  </xsl:choose> 
                </td>

                <td>
                    <xsl:choose>
                        <xsl:when test="dayOfWeek = 'Mon'">
                            <xsl:value-of select="concat(lowest,'°-',highest, '°')"/>
                            <br/>
                            <xsl:choose>
                                <xsl:when test="overallCode = 'cloudy'">
                                    <img src="cloudy.jpeg" height="70" width="90" />
                                    <br/>
                                    <span style="color:blue">
                                    <xsl:value-of select="overall"/>
                                    </span>                        
                                </xsl:when>
                                <xsl:when test="overallCode = 'partlySunny'">
                                    <img src="partlySunny.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'rain'">
                                    <img src="rain.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'sunny'">
                                    <img src="sunny.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'thunderstorm'">
                                    <img src="thunderstorm.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                            </xsl:choose>
                        </xsl:when>
                        <xsl:otherwise> </xsl:otherwise>
                    </xsl:choose>
                </td>

                <td>
                    <xsl:choose>
                        <xsl:when test="dayOfWeek = 'Tues'">
                            <xsl:value-of select="concat(lowest,'°-',highest, '°')"/>
                            <br/>
                            <xsl:choose>
                                <xsl:when test="overallCode = 'cloudy'">
                                    <img src="cloudy.jpeg" height="70" width="90" />
                                    <br/>
                                    <span style="color:blue">
                                    <xsl:value-of select="overall"/>
                                    </span>                        
                                </xsl:when>
                                <xsl:when test="overallCode = 'partlySunny'">
                                    <img src="partlySunny.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'rain'">
                                    <img src="rain.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'sunny'">
                                    <img src="sunny.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'thunderstorm'">
                                    <img src="thunderstorm.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                            </xsl:choose>
                        </xsl:when>
                        <xsl:otherwise> </xsl:otherwise>
                    </xsl:choose>
                </td>

                <td>  
                    <xsl:choose>
                        <xsl:when test="dayOfWeek = 'Wed'">
                            <xsl:value-of select="concat(lowest,'°-',highest, '°')"/>
                            <br/>
                            <xsl:choose>
                                <xsl:when test="overallCode = 'cloudy'">
                                    <img src="cloudy.jpeg" height="70" width="90" />
                                    <br/>
                                    <span style="color:blue">
                                    <xsl:value-of select="overall"/>
                                    </span>                        
                                </xsl:when>
                                <xsl:when test="overallCode = 'partlySunny'">
                                    <img src="partlySunny.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'rain'">
                                    <img src="rain.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'sunny'">
                                    <img src="sunny.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'thunderstorm'">
                                    <img src="thunderstorm.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                            </xsl:choose>
                        </xsl:when>
                        <xsl:otherwise> </xsl:otherwise>
                    </xsl:choose>
                </td>

                <td>
                    <xsl:choose>
                        <xsl:when test="dayOfWeek = 'Thu'">
                            <xsl:value-of select="concat(lowest,'°-',highest, '°')"/>
                            <br/>
                            <xsl:choose>
                                <xsl:when test="overallCode = 'cloudy'">
                                    <img src="cloudy.jpeg" height="70" width="90" />
                                    <br/>
                                    <span style="color:blue">
                                    <xsl:value-of select="overall"/>
                                    </span>                        
                                </xsl:when>
                                <xsl:when test="overallCode = 'partlySunny'">
                                    <img src="partlySunny.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'rain'">
                                    <img src="rain.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'sunny'">
                                    <img src="sunny.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'thunderstorm'">
                                    <img src="thunderstorm.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                            </xsl:choose>
                        </xsl:when>
                        <xsl:otherwise> </xsl:otherwise>
                    </xsl:choose>
                </td>

                <td>
                    <xsl:choose>
                        <xsl:when test="dayOfWeek = 'Fri'">
                            <xsl:value-of select="concat(lowest,'°-',highest, '°')"/>
                            <br/>
                            <xsl:choose>
                                <xsl:when test="overallCode = 'cloudy'">
                                    <img src="cloudy.jpeg" height="70" width="90" />
                                    <br/>
                                    <span style="color:blue">
                                    <xsl:value-of select="overall"/>
                                    </span>                        
                                </xsl:when>
                                <xsl:when test="overallCode = 'partlySunny'">
                                    <img src="partlySunny.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'rain'">
                                    <img src="rain.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'sunny'">
                                    <img src="sunny.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'thunderstorm'">
                                    <img src="thunderstorm.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                            </xsl:choose>
                        </xsl:when>
                        <xsl:otherwise> </xsl:otherwise>
                    </xsl:choose>
                </td>

                <td>
                    <xsl:choose>
                        <xsl:when test="dayOfWeek = 'Sat'">
                            <xsl:value-of select="concat(lowest,'°-',highest, '°')"/>
                            <br/>
                            <xsl:choose>
                                <xsl:when test="overallCode = 'cloudy'">
                                    <img src="cloudy.jpeg" height="70" width="90" />
                                    <br/>
                                    <span style="color:blue">
                                    <xsl:value-of select="overall"/>
                                    </span>                        
                                </xsl:when>
                                <xsl:when test="overallCode = 'partlySunny'">
                                    <img src="partlySunny.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'rain'">
                                    <img src="rain.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'sunny'">
                                    <img src="sunny.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'thunderstorm'">
                                    <img src="thunderstorm.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                            </xsl:choose>
                        </xsl:when>
                        <xsl:otherwise> </xsl:otherwise>
                    </xsl:choose>
                </td>
                
                <td>
                    <xsl:choose>
                        <xsl:when test="dayOfWeek = 'Sun'">
                            <xsl:value-of select="concat(lowest,'°-',highest, '°')"/>
                            <br/>
                            <xsl:choose>
                                <xsl:when test="overallCode = 'cloudy'">
                                    <img src="cloudy.jpeg" height="70" width="90" />
                                    <br/>
                                    <span style="color:blue">
                                    <xsl:value-of select="overall"/>
                                    </span>                        
                                </xsl:when>
                                <xsl:when test="overallCode = 'partlySunny'">
                                    <img src="partlySunny.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'rain'">
                                    <img src="rain.jpeg" height="70" width="100" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'sunny'">
                                    <img src="sunny.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:red">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                                <xsl:when test="overallCode = 'thunderstorm'">
                                    <img src="thunderstorm.jpeg" height="70" width="80" />
                                    <br/>
                                    <span style="color:orange">
                                    <xsl:value-of select="overall"/>
                                    </span>
                                </xsl:when>
                            </xsl:choose>
                        </xsl:when>
                        <xsl:otherwise> </xsl:otherwise>
                    </xsl:choose>
                </td>
          
              </tr>
            </xsl:for-each>
          </table>
        </div>
      </body>
    </html>
  </xsl:template> 
</xsl:stylesheet>