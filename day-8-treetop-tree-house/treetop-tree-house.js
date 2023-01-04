const treeMap = [
    "200200221023111313131033314121142013103432145142351212334232423210101340410243413011333312111010010",
    "021002023301222221234134021422342024344555521535143232341414552024224120114233210330203002020100112",
    "120000123021210023111321143114331115334535223455511513445233523154411102203411040133312002213001021",
    "110211312303200204232110124204135453554533435152342542252215415141133330323032234114310011301232202",
    "112002122201001100330432244432552555524445123151222142521452233321152332132412434434431321322021220",
    "000131233030332102140440124221314455255431113413445553414144524134315351524134030112312012102102122",
    "011002120310213142402320144522121125454423123245535451115134412543215113433312403430132101003202030",
    "001221312201314442411333454131552331253553254425236334643151355314514413411344034432330410221101023",
    "133033302114012204213054544541124453214232545523665466356466451514332142121512400041213432211332332",
    "122103100320433433403313515121232352332442555253656542336644235234542522322522414400320014312110331",
    "220032121143103434234531224315451255225362634256634623342624242245654341134514413144333113211200033",
    "320112113344013332224131114231235263526556625325625352254643224563365551253353323542200003301120011",
    "130332114433413215333445212514445445656665256554333534422554442522234433415533124353022320300112030",
    "122220320003402342433443415465352622564252264442264334335624365224645544545412124352220434440211220",
    "012123032311134245212342233263346563632453535355553473445564362634252543555515242444423232000444220",
    "210332422344222154315435122245243633424643346345734336333746422324336263624544151122442021330341202",
    "122113144440445232235222443563362625543565533465377647363543377645634552632254214531354231413432430",
    "312340402310532324322313244522226622547366756445444754767335355365264622465662241215332253310001232",
    "203342203201331433144542522354633356376457563745333765735577477354743263423666625212251354244021004",
    "023132211325442531332565334564256663665357767653737436565453774766335532544656254552332354313323032",
    "104344140125552254523443534436547653753334746356364664565677777637444474643245425325454224440231203",
    "030303323422144551254256535247737377634445575474654433333453643564664344462332353234553115322142242",
    "043342223454513255464263333566337576377476354884845654658465735544446646436232534263314313142020101",
    "340311214411551345423466343646644336367654787858788857666654635337366537645634644263323112331404131",
    "040141315333331565455545334767475747755574585547567756844746644445646736447635456236413253453410130",
    "211021153443415666656253646443465373878486485664464485545486846643475567536535465634262415153200040",
    "434443334231526223353563373464374574547886487867474546748668788886554566336675234542522151345414431",
    "342100553111533623655466757467553555676668887764575574556755884875687334634675256256443425223423211",
    "421145141552463255552236436455476686566587654558577848647854485587448337355756554555544211113112433",
    "401034232152434624233754647737667758845867866675595798957488447876578774367337742646625521543244120",
    "201414142512656264345465456536564477766677986565767776589758477664747866666435364642236343442335143",
    "422042442525465325256445643735574646548578959977866889666586787677748745536646677524242544332243420",
    "101531424154626224664754337344565457557999965875599965977796778866568855445766577565632633451545144",
    "111515354125252635577747557658555488765757696767797558565755699985844788764347763523465333315513212",
    "222334234142233522754645544788567846579566995878775676667979868685866578655574543564453254615121150",
    "121552233464445256557546467767485865866888757989977669966767877786686475874646454752632664243132511",
    "412242332564644335747746348878865677677797755798669796798699855757865564547645373677564252625352445",
    "104135225262634344357677645645458796767865979969889676688676788669777674757634454746666526341145313",
    "021542323626266573437334685574765967759968767697666876767887775889896866845887736736426556541522241",
    "321245255565266675757675486554868969567677786789686889669988776968557656488476534636744443443445532",
    "424153123565322534465577464547665888797687899787966868666667897595997786576655333657432563645515114",
    "151513345354454444763668544475487669995769769878776696968966788666679588686556634737544644543232332",
    "315411214333624753546345646876778875556666766899787967667988799866697798768788653774352466325322155",
    "411515135354235576553778556478657685968679689776697889878966888788686556488744645555636235464132151",
    "521535123365535747465567756884789758877668899777979788877786896957896655744848765333672323354342345",
    "511122245466262643344764588545559786677866787999989789989769786875585659588677463454335226643415231",
    "234355522634365636744684556586586576767676868898988888987788888877768767654646777776645642226512141",
    "113123464223654555566666486667798785887896678897787899778677766996769787745467865757755656543512345",
    "513251343243554753654655574645569758987667887877878998789898989677659987488676836733553556554225344",
    "514313564242345475335768454478576556889868687997999987778988866675979779845785867656464634654245123",
    "114315542426623675675378664848688856798777688977789877988898769769667968885864643357435456442515251",
    "342223563236537773664686558445968779787887987788777777899877867865678669767686535536743642245412355",
    "125543254543547353647388564555887588899766978788778797797796898997787999888766547554567344424443422",
    "235522554554262346774664445787579599869688998989778778978989968998575857577865454747575353226552114",
    "222421136654623646474466478475666768686777899887878779887688896658596779765485853765563356364225314",
    "521231534444644737467764858748655998796879877877788879799986898965697856444748453437553352232525543",
    "451421316463534654736364878868555996777987969978898798976796968858967778666788533743354325346223354",
    "353521254635223475773456867765596786879787787769889887896999898885688596454456655466765442452131244",
    "112452332645434776643548885574558878789797669769989989886877966757566586444578445673434665652431423",
    "125112515242255354574555588568695879785886989867778677698879979576678878668587547744623644323213555",
    "222335123454333544773645644774469985799577787667779799699876685666756857858446357667422332624342332",
    "342124352633564466565447655564575889567797869876686996679999868665879886844677564455723264641334552",
    "211531121363532576364535865484865759689798698998996686966767965765789787447464533667726322444223531",
    "003112555432534436636776465475555776887557956877687879969697585659596546865447775565562326263355343",
    "433244413454525566563634447454784577659787856568996976596789778896764874668454673456462646455545115",
    "315114535444536635475346535567864558579958679557799758766667597987857466754537555645552424625323424",
    "041544243435426366744535764674465545875655656695956899997569789788477547755346553676234364525135211",
    "110125213453624243247556736654454474595787967599557857997699578855767558775435554762633446551353134",
    "230513132216566245267463366654684755868756978975659588575959655686655788733345435522656542222543322",
    "042134352115436525535436657767864645756586865777685969969787676584458468744346376522324323225232212",
    "113011555414226244554676353335845564485568555689599656977797776777868787473376444245355443123441231",
    "141222553351554636564756467565656675455484874698998587887767666457458846465776554544333612224555323",
    "410201213345143434422573347343756574748746464486554485756685477655667634334766422236535313341542224",
    "400013155121116452255553534765374544884448574876457458645878446585657476536357256436654223345343132",
    "142320132432156443246333547553474375466866456765867768748787675644755677446563663223424341524352200",
    "130310433221343524424456477364543647448885475465487864674454548867635637545422424333245424354220221",
    "104443025533452125362252625375463664447488646447874885476567646456653665465543643663511122334514003",
    "302020415314212533664642446555554345445458887778858887685645576353536647674424342553325334543032421",
    "241431045353353251642363462546445336355737566757557674865573447644353353564422462552323432524142311",
    "123213233322144323666345645436644754537635574357377674465747755476333656624223243445125521412332331",
    "012331042212144212425325652566536457633744775665435737646677453634637335562564643341411132411032042",
    "312330023343231454516256365325363757435647543374644573757667446466553456424326532235455225410011222",
    "330440423204155515131264636336326536353437335474474464535536754457526344465446535213522513202431334",
    "111010303340451214252454445262262654354536464545434674354557674362552463364322545323344220103312142",
    "011012340310414525221212256242445654336566374374366636534765356655652454533664444453134140113204011",
    "230024312112245355233251252646423364546365646735756334573543653656365434363633141223321213032042131",
    "031001023032240425233144214253446244556226622634747362226456645266342264223215113131540112130410110",
    "322123043034044225552242443355356433432465646225242242422346453346634325254325435535313321413201023",
    "022331002231110112224233354325624225342363424426633436565344545533465463152555421312331102120410200",
    "013020314334233240543141441351342432435423252532545655664253435662546145412112135314414140233322202",
    "023101011114024240134343343214355543453244325544366633232356362353335431215322232434231302030012200",
    "121203223241323132430512521115213312263253263242264335335446352453314333354413113210133333212120303",
    "102030123234100043232214342352345452215246465634534464364425653323345231332311444434220444330131120",
    "000331303323044244144032522114521112125142214553424464423124453113211413324230342333130021200000221",
    "121203123313224230334312325441234431451535345453515132125413445443323514321330302200100022013232311",
    "000221331111234212331404233225332533323225131525322111443344452254442544201223424140243032213101301",
    "010202021330012103042021024434411545123253214353525251521434235541535344240243403200122322133122101",
    "121102231211003113342040440404003344542241345133131133414435235243325441120032344431223311313111221",
    "011210032333020312123124101444102341443212553521355222414135533333310320012002223342012031112321112"
];

const treeGrid = treeMap.map(row => row.split(""));
const isVisible = [];

const visibilityDistanceTowardsLeft = [];
const visibilityDistanceTowardsRight = [];
const visibilityDistanceTowardsTop = [];
const visibilityDistanceTowardsBottom = [];

const totalRows = treeGrid.length;
const totalCols = treeGrid[0].length;

function findContinuousSmallerTreesInDirection(currentRow, currentCol, direction) {
    const currentTreeSize = treeGrid[currentRow][currentCol];

    let count = 0;
    if (direction === 0) { // Towards Bottom
        if (currentRow == totalRows - 1) {
            return 0;
        }
        for (let row = currentRow + 1; row < totalRows; row++) {
            count++;
            if (currentTreeSize <= treeGrid[row][currentCol]) {
                break;
            }
        }
    } else if (direction === 1) { // Towards Top
        if (currentRow == 0) {
            return 0;
        }
        for (let row = currentRow - 1; row >= 0; row--) {
            count++;
            if (currentTreeSize <= treeGrid[row][currentCol]) {
                break;
            }
        }
    } else if (direction === 2) { // Towards Right
        if (currentCol == totalCols - 1) {
            return 0;
        }
        for (let col = currentCol + 1; col < totalCols; col++) {
            count++;
            if (currentTreeSize <= treeGrid[currentRow][col]) {
                break;
            }
        }
        
    } else { // Towards Left
        if (currentCol == 0) {
            return 0;
        }
        for (let col = currentCol - 1; col >= 0; col--) {
            count++;
            if (currentTreeSize <= treeGrid[currentRow][col]) {
                break;
            }
        }
    }
    return count;
}

for (let row = 0; row < totalRows; row++) {
    const isVisibleRowData = [];
    const visibilityDistanceTowardsLeftRowData = [];
    const visibilityDistanceTowardsRightRowData = [];
    const visibilityDistanceTowardsTopRowData = [];
    const visibilityDistanceTowardsBottomRowData = [];
    for (let col = 0; col < totalCols; col++) {
        visibilityDistanceTowardsLeftRowData.push(0);
        visibilityDistanceTowardsRightRowData.push(0);
        visibilityDistanceTowardsTopRowData.push(0);
        visibilityDistanceTowardsBottomRowData.push(0);

        if (row == 0 || row == totalRows - 1 || col == 0 || col == totalCols -1) {
            isVisibleRowData.push(1);
        } else {
            isVisibleRowData.push(0);
        }   
    }
    visibilityDistanceTowardsLeft.push(visibilityDistanceTowardsLeftRowData);
    visibilityDistanceTowardsRight.push(visibilityDistanceTowardsRightRowData);
    visibilityDistanceTowardsTop.push(visibilityDistanceTowardsTopRowData);
    visibilityDistanceTowardsBottom.push(visibilityDistanceTowardsBottomRowData);
    isVisible.push(isVisibleRowData);
}

// Row wise, left to right
for (let row = 0; row < totalRows; row++) {
    let maxSoFar = treeGrid[row][0];
    for (let col = 0; col < totalCols; col++) {
        if (maxSoFar < treeGrid[row][col]) {
            isVisible[row][col] = 1;
            maxSoFar = treeGrid[row][col];
        }
    }
}

// Row wise, right to left
for (let row = 0; row < totalRows; row++) {
    let maxSoFar = treeGrid[row][totalCols - 1];
    for (let col = totalCols - 1; col > 0; col--) {
        if (maxSoFar < treeGrid[row][col]) {
            isVisible[row][col] = 1;
            maxSoFar = treeGrid[row][col];
        }
    }
}

// Col wise, top to bottom
for (let col = 0; col < totalCols; col++) {
    let maxSoFar = treeGrid[0][col];
    for (let row = 0; row < totalRows; row++) {
        if (maxSoFar < treeGrid[row][col]) {
            isVisible[row][col] = 1;
            maxSoFar = treeGrid[row][col];
        }
    }
}

// Col wise, bottom to top
for (let col = 0; col < totalCols; col++) {
    let maxSoFar = treeGrid[totalRows - 1][col];
    for (let row = totalRows - 1; row > 0; row--) {
        if (maxSoFar < treeGrid[row][col]) {
            isVisible[row][col] = 1;
            maxSoFar = treeGrid[row][col];
        }
    }
}

let totalScenicScore = 0;
for (let row = 0; row < totalRows; row++) {
    for (let col = 0; col < totalCols; col++) {
        visibilityDistanceTowardsLeft[row][col] = findContinuousSmallerTreesInDirection(row, col, 3);
        visibilityDistanceTowardsRight[row][col] = findContinuousSmallerTreesInDirection(row, col, 2);
        visibilityDistanceTowardsTop[row][col] = findContinuousSmallerTreesInDirection(row, col, 1);
        visibilityDistanceTowardsBottom[row][col] = findContinuousSmallerTreesInDirection(row, col, 0);

        const newScenicScore = visibilityDistanceTowardsBottom[row][col] * visibilityDistanceTowardsTop[row][col] * visibilityDistanceTowardsRight[row][col] * visibilityDistanceTowardsLeft[row][col];
        if (newScenicScore > totalScenicScore ) {
            totalScenicScore = newScenicScore;
        }
    }
}

let total = 0;
for (let row = 0; row < totalRows; row++) {
    for (let col = 0; col < totalCols; col++) {
        total += isVisible[row][col];
    }
}


console.log(total);
console.log(totalScenicScore);