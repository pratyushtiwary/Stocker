def render_block(title,pub_date,link):
  block = """
  <table
    align="center"
    border="0"
    cellpadding="0"
    cellspacing="10"
    class="row row-2"
    role="presentation"
    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
    width="100%"
  >
    <tbody>
      <tr>
        <td>
          <table
            align="center"
            border="0"
            cellpadding="0"
            cellspacing="0"
            class="row-content stack"
            role="presentation"
            style="
              mso-table-lspace: 0pt;
              mso-table-rspace: 0pt;
              color: #000000;
              width: 500px;
            "
            width="500"
          >
            <tbody>
              <tr>
                <td
                  class="column column-1"
                  style="
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                    font-weight: 400;
                    text-align: left;
                    vertical-align: top;
                    border-bottom: 1px solid #000000;
                    border-left: 1px solid #000000;
                    border-right: 1px solid #000000;
                    border-top: 1px solid #000000;
                    padding-top: 5px;
                    border-radius: 5px;
                    padding-bottom: 5px;
                  "
                  width="100%"
                >
                  <table
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="heading_block"
                    role="presentation"
                    style="
                      mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                    "
                    width="100%"
                  >
                    <tr>
                      <td
                        style="
                          width: 100%;
                          text-align: center;
                          padding-left: 15px;
                        "
                      >
                        <h2
                          style="
                            margin: 0;
                            color: #555555;
                            font-size: 18px;
                            font-family: Arial, Helvetica Neue,
                              Helvetica, sans-serif;
                            line-height: 120%;
                            text-align: left;
                            direction: ltr;
                            font-weight: 700;
                            letter-spacing: normal;
                            margin-top: 0;
                            margin-bottom: 0;
                          "
                        >
                          """+title+"""
                        </h2>
                      </td>
                    </tr>
                  </table>
                  <table
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="heading_block"
                    role="presentation"
                    style="
                      mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                    "
                    width="100%"
                  >
                    <tr>
                      <td
                        style="
                          width: 100%;
                          text-align: center;
                          padding-left: 15px;
                        "
                      >
                        <h3
                          style="
                            margin: 0;
                            color: #555555;
                            font-size: 14px;
                            font-family: Arial, Helvetica Neue,
                              Helvetica, sans-serif;
                            line-height: 120%;
                            text-align: left;
                            direction: ltr;
                            font-weight: 700;
                            letter-spacing: normal;
                            margin-top: 0;
                            margin-bottom: 0;
                          "
                        >
                          """+pub_date+"""
                        </h3>
                      </td>
                    </tr>
                  </table>
                  <table
                    border="0"
                    cellpadding="10"
                    cellspacing="0"
                    class="button_block"
                    role="presentation"
                    style="
                      mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                    "
                    width="100%"
                  >
                    <tr>
                      <td>
                        <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" style="height:42px;width:119px;v-text-anchor:middle;" arcsize="10%" stroke="false" fillcolor="#f08c11"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Arial, sans-serif; font-size:16px"><![endif]-->
                        <a
                          href=\""""+link+""""\"
                          style="
                            text-decoration: none;
                            display: inline-block;
                            color: #ffffff;
                            background-color: #f08c11;
                            border-radius: 4px;
                            width: auto;
                            border-top: 1px solid #f08c11;
                            border-right: 1px solid #f08c11;
                            border-bottom: 1px solid #f08c11;
                            border-left: 1px solid #f08c11;
                            padding-top: 5px;
                            padding-bottom: 5px;
                            font-family: Arial, Helvetica Neue,
                              Helvetica, sans-serif;
                            text-align: center;
                            mso-border-alt: none;
                            word-break: keep-all;
                          "
                        >
                          <span
                            style="
                              padding-left: 20px;
                              padding-right: 20px;
                              font-size: 16px;
                              display: inline-block;
                              letter-spacing: normal;
                            "
                            ><span
                              style="
                                font-size: 16px;
                                line-height: 2;
                                word-break: break-word;
                                mso-line-height-alt: 32px;
                              "
                              >Read More</span
                            ></span
                          >
                        </a>
                        <!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
  """
  return block

def render_mail_template(nse_announcements,bse_notices):
  nse_block = ""
  bse_block = ""


  for block in nse_announcements:
    nse_block += render_block(block["title"],block["pubDate"],block["link"])

  for block in bse_notices:
    bse_block += render_block(block["title"],block["pubDate"],block["link"])


  mail_template = """
    <!DOCTYPE html>

    <html
      lang="en"
      xmlns:o="urn:schemas-microsoft-com:office:office"
      xmlns:v="urn:schemas-microsoft-com:vml"
    >
      <head>
        <title></title>
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
        <meta content="width=device-width, initial-scale=1.0" name="viewport" />
        <!--[if mso
          ]><xml
            ><o:OfficeDocumentSettings
              ><o:PixelsPerInch>96</o:PixelsPerInch
              ><o:AllowPNG /></o:OfficeDocumentSettings></xml
        ><![endif]-->
        <style>
          * {
            box-sizing: border-box;
          }

          body {
            margin: 0;
            padding: 0;
          }

          a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: inherit !important;
          }

          #MessageViewBody a {
            color: inherit;
            text-decoration: none;
          }

          p {
            line-height: inherit;
          }

          @media (max-width: 520px) {
            .icons-inner {
              text-align: center;
            }

            .icons-inner td {
              margin: 0 auto;
            }

            .row-content {
              width: 100% !important;
            }

            .image_block img.big {
              width: auto !important;
            }

            .column .border {
              display: none;
            }

            .stack .column {
              width: 100%;
              display: block;
            }
          }
        </style>
      </head>
      <body
        style="
          background-color: #ffffff;
          margin: 0;
          padding: 0;
          -webkit-text-size-adjust: none;
          text-size-adjust: none;
        "
      >
        <table
          border="0"
          cellpadding="0"
          cellspacing="0"
          class="nl-container"
          role="presentation"
          style="
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
            background-color: #ffffff;
          "
          width="100%"
        >
          <tbody>
            <tr>
              <td>
                <table
                  align="center"
                  border="0"
                  cellpadding="0"
                  cellspacing="0"
                  class="row row-1"
                  role="presentation"
                  style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
                  width="100%"
                >
                  <tbody>
                    <tr>
                      <td>
                        <table
                          align="center"
                          border="0"
                          cellpadding="0"
                          cellspacing="0"
                          class="row-content stack"
                          role="presentation"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            color: #000000;
                            width: 500px;
                          "
                          width="500"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="column column-1"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  font-weight: 400;
                                  text-align: left;
                                  vertical-align: top;
                                  padding-top: 5px;
                                  padding-bottom: 5px;
                                  border-top: 0px;
                                  border-right: 0px;
                                  border-bottom: 0px;
                                  border-left: 0px;
                                "
                                width="100%"
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  class="heading_block"
                                  role="presentation"
                                  style="
                                    mso-table-lspace: 0pt;
                                    mso-table-rspace: 0pt;
                                  "
                                  width="100%"
                                >
                                  <tr>
                                    <td style="width: 100%; text-align: center">
                                      <h1
                                        style="
                                          margin: 0;
                                          color: #555555;
                                          font-size: 34px;
                                          font-family: Arial, Helvetica Neue,
                                            Helvetica, sans-serif;
                                          line-height: 120%;
                                          text-align: center;
                                          direction: ltr;
                                          font-weight: 700;
                                          letter-spacing: normal;
                                          margin-top: 0;
                                          margin-bottom: 0;
                                        "
                                      >
                                        <strong>Stocker</strong>
                                      </h1>
                                    </td>
                                  </tr>
                                </table>
                                <table
                                  border="0"
                                  cellpadding="10"
                                  cellspacing="0"
                                  class="divider_block"
                                  role="presentation"
                                  style="
                                    mso-table-lspace: 0pt;
                                    mso-table-rspace: 0pt;
                                  "
                                  width="100%"
                                >
                                  <tr>
                                    <td>
                                      <div align="center">
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                          style="
                                            mso-table-lspace: 0pt;
                                            mso-table-rspace: 0pt;
                                          "
                                          width="100%"
                                        >
                                          <tr>
                                            <td
                                              class="divider_inner"
                                              style="
                                                font-size: 1px;
                                                line-height: 1px;
                                                border-top: 1px solid #bbbbbb;
                                              "
                                            >
                                              <span> </span>
                                            </td>
                                          </tr>
                                        </table>
                                      </div>
                                    </td>
                                  </tr>
                                </table>
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  class="heading_block"
                                  role="presentation"
                                  style="
                                    mso-table-lspace: 0pt;
                                    mso-table-rspace: 0pt;
                                  "
                                  width="100%"
                                >
                                  <tr>
                                    <td style="width: 100%; text-align: center">
                                      <h2
                                        style="
                                          margin: 0;
                                          color: #555555;
                                          font-size: 23px;
                                          font-family: Arial, Helvetica Neue,
                                            Helvetica, sans-serif;
                                          line-height: 120%;
                                          text-align: center;
                                          direction: ltr;
                                          font-weight: 700;
                                          letter-spacing: normal;
                                          margin-top: 0;
                                          margin-bottom: 0;
                                        "
                                      >
                                        NSE Announcements
                                      </h2>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
                """+nse_block+"""

                <table
                          align="center"
                          border="0"
                          cellpadding="0"
                          cellspacing="0"
                          class="row-content stack"
                          role="presentation"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            color: #000000;
                            width: 500px;
                          "
                          width="500"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="column column-1"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  font-weight: 400;
                                  text-align: left;
                                  vertical-align: top;
                                  padding-top: 5px;
                                  padding-bottom: 5px;
                                  border-top: 0px;
                                  border-right: 0px;
                                  border-bottom: 0px;
                                  border-left: 0px;
                                "
                                width="100%"
                              >
                              <table
                                  border="0"
                                  cellpadding="10"
                                  cellspacing="0"
                                  class="divider_block"
                                  role="presentation"
                                  style="
                                    mso-table-lspace: 0pt;
                                    mso-table-rspace: 0pt;
                                  "
                                  width="100%"
                                >
                                  <tr>
                                    <td>
                                      <div align="center">
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                          style="
                                            mso-table-lspace: 0pt;
                                            mso-table-rspace: 0pt;
                                          "
                                          width="100%"
                                        >
                                          <tr>
                                            <td
                                              class="divider_inner"
                                              style="
                                                font-size: 1px;
                                                line-height: 1px;
                                                border-top: 1px solid #bbbbbb;
                                              "
                                            >
                                              <span> </span>
                                            </td>
                                          </tr>
                                        </table>
                                      </div>
                                    </td>
                                  </tr>
                                </table>
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  class="heading_block"
                                  role="presentation"
                                  style="
                                    mso-table-lspace: 0pt;
                                    mso-table-rspace: 0pt;
                                  "
                                  width="100%"
                                >
                                  <tr>
                                    <td style="width: 100%; text-align: center">
                                      <h2
                                        style="
                                          margin: 0;
                                          color: #555555;
                                          font-size: 23px;
                                          font-family: Arial, Helvetica Neue,
                                            Helvetica, sans-serif;
                                          line-height: 120%;
                                          text-align: center;
                                          direction: ltr;
                                          font-weight: 700;
                                          letter-spacing: normal;
                                          margin-top: 0;
                                          margin-bottom: 0;
                                        "
                                      >
                                        BSE Notices
                                      </h2>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>

                """+bse_block+"""

                <table
                  align="center"
                  border="0"
                  cellpadding="0"
                  cellspacing="0"
                  class="row row-3"
                  role="presentation"
                  style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
                  width="100%"
                >
                  <tbody>
                    <tr>
                      <td>
                        <table
                          align="center"
                          border="0"
                          cellpadding="0"
                          cellspacing="0"
                          class="row-content stack"
                          role="presentation"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            color: #000000;
                            width: 500px;
                          "
                          width="500"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="column column-1"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  font-weight: 400;
                                  text-align: left;
                                  vertical-align: top;
                                  padding-top: 5px;
                                  padding-bottom: 5px;
                                  border-top: 0px;
                                  border-right: 0px;
                                  border-bottom: 0px;
                                  border-left: 0px;
                                "
                                width="100%"
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  class="icons_block"
                                  role="presentation"
                                  style="
                                    mso-table-lspace: 0pt;
                                    mso-table-rspace: 0pt;
                                  "
                                  width="100%"
                                >
                                  <tr>
                                    <td
                                      style="
                                        vertical-align: middle;
                                        color: #9d9d9d;
                                        font-family: inherit;
                                        font-size: 15px;
                                        padding-bottom: 5px;
                                        padding-top: 5px;
                                        text-align: center;
                                      "
                                    >
                                      <table
                                        cellpadding="0"
                                        cellspacing="0"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                        "
                                        width="100%"
                                      >
                                        <tr>
                                          <td
                                            style="
                                              vertical-align: middle;
                                              text-align: center;
                                            "
                                          >
                                            <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
                                            <!--[if !vml]><!-->
                                            <table
                                              cellpadding="0"
                                              cellspacing="0"
                                              class="icons-inner"
                                              role="presentation"
                                              style="
                                                mso-table-lspace: 0pt;
                                                mso-table-rspace: 0pt;
                                                display: inline-block;
                                                margin-right: -4px;
                                                padding-left: 0px;
                                                padding-right: 0px;
                                              "
                                            >
                                              <!--<![endif]-->
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- End -->
      </body>
    </html>
  """

  return mail_template
